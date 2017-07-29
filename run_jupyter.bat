@rem ====================
@rem Run jupyter-notebook
@rem ====================
set ENV=env

call %ENV%\Scripts\activate.bat
jupyter-notebook
