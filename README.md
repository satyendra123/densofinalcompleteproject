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


Note- make the exe of you backned
1) make one file named run_server.py and put this code
# run_server.py
from waitress import serve
from denso.wsgi import application
import logging
print("🔧 Starting Waitress server on http://0.0.0.0:8000")
# Optional: enable Waitress logs
logging.basicConfig(level=logging.INFO)
serve(application, host='0.0.0.0', port=8000)

1) venv\Scripts\activate
2) make the exe
pyinstaller --onefile --noconsole ^
--hidden-import=authentication ^
--hidden-import=authentication.apps ^
--hidden-import=authentication.urls ^
--hidden-import=rfid_esd ^
--hidden-import=rfid_esd.apps ^
--hidden-import=rfid_esd.urls ^
--hidden-import=dj_rest_auth ^
--hidden-import=dj_rest_auth.registration ^
--hidden-import=allauth ^
--hidden-import=allauth.account ^
--hidden-import=allauth.socialaccount ^
--hidden-import=rest_framework ^
run_server.py

how to setup django backened code in services so that it runs in the background

step-1 we have the backened exe
step-2 after making the backened exe i want to make the services of this exe so to make it. open the cmd in the administrator
a) nssm install MyPythonService
b) so one gui is open then i will select the my exe and write the services name densobackenedservices now i need to make the start the services
c) nssm start densobackenedservices
d) for stop the services sc stop densobackenedservices
e) for deleting the services sc delete densobackenedservices

so backened services is done and also working


2)
a) not make the services for the frotened when made by the vite.
i have made paramount controller for controlling the barrier

frontened ka exe kaise banate hai. so hum windows ke exe ke liye electron ka use karte hai. lekin agar hum chahte hai ki mera ek exe ho jisse mera frontened windows me open na hokar browser me open ho to mujhe ye chiz apply karni padegi.

step-0) npm install -g pkg step-1) npm install serve-handler step-2) sabse pahle ek server.js ke name se file banao. jo ki main project ke andar ye file rahegi.

const { exec } = require('child_process'); exec('npx serve -s dist -l 3000'); exec('start http://localhost:3000');

step-3) run the npm run build.

step-4) pkg server.js --targets node18-win-x64 --output SaralaxeIndia.exe

step-5) agar hume client ka image se exe banani hai to hum wo bhi kar sakte hai

step-6) isko run krne ke liye dist folder chahiye aur dist folder ke bahar ye meri exe hono chahiye tbhi ye exe jo hai dist folder me jo files hai unko serve karti hai browser me means ki meri website ko, aur mera package.json file bhi hona chahiye dependency ke liye. so agar mujhe kisi client ke pc me ye chiz dalni hai to mere pass dist folder, exe aur package.json file hona chahiye

b)
not make the services for the frotened when made by the vite.
i have made paramount controller for controlling the barrier

frontened ka exe kaise banate hai. so hum windows ke exe ke liye electron ka use karte hai. lekin agar hum chahte hai ki mera ek exe ho jisse mera frontened windows me open na hokar browser me open ho to mujhe ye chiz apply karni padegi.

step-0) npm install -g pkg step-1) npm install serve-handler step-2) sabse pahle ek server.js ke name se file banao. jo ki main project ke andar ye file rahegi.

const { exec } = require('child_process'); exec('npx serve -s dist -l 3000'); exec('start http://localhost:3000');

step-3) run the npm run build.

step-4) pkg server.js --targets node18-win-x64 --output SaralaxeIndia.exe

step-5) agar hume client ka image se exe banani hai to hum wo bhi kar sakte hai

step-6) isko run krne ke liye dist folder chahiye aur dist folder ke bahar ye meri exe hono chahiye tbhi ye exe jo hai dist folder me jo files hai unko serve karti hai browser me means ki meri website ko, aur mera package.json file bhi hona chahiye dependency ke liye. so agar mujhe kisi client ke pc me ye chiz dalni hai to mere pass dist folder, exe aur package.json file hona chahiye
