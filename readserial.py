print("script start")

try:
    import serial
    import pymysql
    from datetime import datetime
    import time

    print("✅ Imports successful")

    SERIAL_PORT = 'COM7'  # Change as per your port
    BAUD_RATE = 9600
    TIMEOUT = 1

    # === MySQL Connection ===
    try:
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="denso",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.Cursor
        )
        cursor = db.cursor()
        print("✅ Connected to MySQL database using PyMySQL")
    except pymysql.MySQLError as err:
        print(f"❌ Database connection error: {err}")
        input("Press Enter to exit...")
        exit(1)

    # === Serial Port Connection ===
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)
        print(f"✅ Connected to serial port {SERIAL_PORT}")
    except Exception as e:
        print(f"❌ Serial port error: {e}")
        input("Press Enter to exit...")
        exit(1)

    # === Function to Insert or Update RFID ===
    def upsert_rfid(rfid):
        try:
            now = datetime.now()
            check_query = "SELECT id FROM rfid_register WHERE rfid_tag_no = %s"
            cursor.execute(check_query, (rfid,))
            result = cursor.fetchone()

            if result:
                update_query = """
                    UPDATE rfid_register
                    SET active = 1,
                        updated_at = %s,
                        updated_by_id = NULL
                    WHERE rfid_tag_no = %s
                """
                cursor.execute(update_query, (now, rfid))
                print(f"🔄 Updated RFID '{rfid}' at {now}")
            else:
                insert_query = """
                    INSERT INTO rfid_register (rfid_tag_no, active, created_at, updated_at, created_by_id, updated_by_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (rfid, 1, now, now, None, None))
                print(f"➕ Inserted RFID '{rfid}' at {now}")

            db.commit()
        except pymysql.MySQLError as err:
            db.rollback()
            print(f"❌ Database error during upsert: {err}")

    # === Main Loop ===
    print("📡 Waiting for RFID scans... Press Ctrl+C to stop.")
    while True:
        if ser.in_waiting:
            rfid = ser.readline().decode('utf-8', errors='ignore').strip()
            if rfid:
                upsert_rfid(rfid)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 Stopped by user.")

except Exception as e:
    print(f"❌ Unhandled error: {e}")
    input("Press Enter to exit...")

finally:
    try:
        if 'ser' in locals():
            ser.close()
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
        print("✅ Serial and database connections closed.")
    except Exception as e:
        print(f"⚠️ Cleanup error: {e}")
