import pandas as pd

def Articles():
        articles = [
            {
                'id': 1,
                'title': 'Article One',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'author': 'Mondragon',
                'create_date': '18-9-2020'
            },

            {
                'id': 2,
                'title': 'Article Two',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'author': 'Martinez',
                'create_date': '18-9-2020'
            },

            {
                'id': 3,
                'title': 'Article Three',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'author': 'Perez',
                'create_date': '18-9-2020'
            }


        ]


        return articles

df = pd.DataFrame(Articles())
df.to_csv("/app/Data/data.csv", index=False)

def get_data():
    data = pd.read_csv("/app/Data/data.csv")
    return data.to_html()

def add_data(newdata=None, data=None):
    if newdata==None:
        return "No new data"
    data = pd.read_csv("/app/Data/data.csv")
    newdata = pd.DataFrame([newdata])
    datacsv = pd.concat([newdata, data])
    datacsv.sort_values(by="id", inplace=True)
    datacsv.to_csv("/app/Data/data.csv", index=False)

