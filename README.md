# densofinalcompleteproject
we have made the complete denso project with rfid

Note- isme esd ki wajah se sare rs485 heat ho rhe the aur data transfer hona ruk jaa rha tha to iska solution ye nikla ki jo mai esd ka signal utha rha tha pin number 7 se arduino par directly. to mai ab directly naa utha kar waha relay connect kar diya aur ab us relay se signal utha rha hu aur yahi same chiz mai diode laga kar bhi kar sakta hu


step-1) run the apache and mysql in the background as a services
net start MySQL         :: Start MySQL service
net stop MySQL          :: Stop MySQL service
sc delete MySQL         :: Delete the MySQL service (be careful)

step-2) run apache as a services
cd C:\xampp\apache\bin
httpd.exe -k install -n "ApacheXAMPP"
net start ApacheXAMPP

how to setup
1)
backened django exe.
step-1) make the run_server.py code 


step-2 after making the backened exe i want to make the services of this exe so to make it
a) nssm install MyPythonService
b) so one gui is open then i will select the my exe and write the services name densobackenedservices now i need to make the start the services
c) nssm start densobackenedservices

