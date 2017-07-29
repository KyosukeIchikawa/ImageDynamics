@rem ========================
@rem Make virtual environment
@rem ========================
set ENV=env

pip install virtualenv
virtualenv %ENV%
call %ENV%\Scripts\activate.bat

pip install numpy==1.13.1
pip install matplotlib==2.0.2
pip install pandas==0.20.3
pip install tensorflow==1.2.1
pip install Pillow==4.2.1
pip install jupyter==1.0.0
