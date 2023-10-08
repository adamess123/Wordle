import requests


def fetch_random_word(api_url, api_key):
    print("""\

                        ._ o o    /
                        \_`-)|_  /
                    ,""       \ /
                    ,"     |   ಠ ಠ. 
                ,"      ,-\__    `.
                ,"       /     `--._;)
            ,"        /
            ,"         / 
    """)
    print("Waiting on API", end ="")
    while True:
        print("..")
        response = requests.get(api_url, headers={
            'X-Api-Key': api_key
        }).json()

        if len(response["word"]) == 5:
            word = response["word"].lower()
            print()
            return word