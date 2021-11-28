import re
import psycopg2

# ? My modules
from config import config as cf
from modules import get_text


def main():
    # Regex Code
    try:
        text = get_text()
    except UnboundLocalError:
        print('Not Valid URL')
        main()
    
    user_input = input('What do you want to find: ')
    user_regex = re.compile(user_input)
    METACHAR = user_regex.findall(text)
    print(METACHAR)

    CONN = None
    CUR = None
    try:
        CONN = psycopg2.connect(
            host=cf.hostname,
            dbname=cf.database,
            user=cf.username,
            password=cf.pwd,
            port=cf.port_id)

        # cursor
        CUR = CONN.cursor()

        # queries
        INSERT_SCRIPT = 'insert into user_info (URL, text) values ( %s, %s);'
        INSERT_VALUES = (user_input, METACHAR)
        CUR.execute(INSERT_SCRIPT, INSERT_VALUES)

        # commit
        CONN.commit()

    except Exception as error:
        print(error)
    finally:
        # ! ALWAYS CLOSE CONNECTIONS
        if CUR is not None:
            CUR.close()
        if CONN is not None:
            CONN.close()


if __name__ == "__main__":
    main()
    
