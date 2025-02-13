# TG-ollama

### Official docs. for python TG library
````
https://docs.python-telegram-bot.org/en/v21.10/index.html
https://docs.python-telegram-bot.org/en/stable/examples.html
````

````
This is a web project with fronjt-end, backend, mongodb, chromaDB and Ollama
The purpose of project, bot which rgenerates html, css and js codes for front-end and shows it in new page
There you can sign up, sign in, chat with a bot, bot will return html pages and new-tab(you need your browser let open new tabs)
You can watch yout chat history
Add some data to chroma_db
Watch all_data from chroma_db

`````

fistly before run install requirment.txt


        pip install -r requiremnt.txt


We are USING MONGO DB, you will need mongodb and database named ollamaKurbanAit with 2 collections: users, history

The project is done using fastapi, So, open directory in terminal and run


        uvicorn backend.main:app --reload


        OR


        fastapi run .\backend\main.py

Go to browser and open localhost:8000

then you can use this application
