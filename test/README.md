1. RateConfig.py should be configured first
2. DB.py is used to export uncertain rate from DB or import rate result to DB
3. Rate.py is the auto script
    a. It could read DB for uncertain rate and write result back to DB if file path is not defined in RateConfig.py
    b. If file path is defined, it will work on file instead of DB
4. The exported uncertain rate file is like "e_data"
5. The result rate file is like "i_data"
