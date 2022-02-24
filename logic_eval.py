import pandas as pd
import csv
import os

class Logic_eval:

    tables = {}

    op = {
        "LOAD" : lambda arg : Logic_eval.load(arg),
        "SHOW" : lambda arg : Logic_eval.show(arg),
        "CREATE" : lambda arg : Logic_eval.create(arg),
        "DROP" : lambda arg : Logic_eval.drop(arg),
        "COMMENT" : lambda arg : Logic_eval.comment(arg),
        "SAVE" : lambda arg : Logic_eval.save(arg),
        "ALTER" : lambda arg : Logic_eval.alter(arg),
        "PROCEDURE" : lambda arg : Logic_eval.procedure(arg),
        "SELECT" : lambda arg : Logic_eval.select(arg),
    }

    @staticmethod
    def load(args):

        try:
            table = args['Table']
            csv = args['csv']
        except KeyError:
            raise KeyError('Table was not found')

        try:
            df = pd.read_csv(csv)

        except KeyError:
            raise KeyError('Something went wrong')

        if table in Logic_eval.tables.keys():
            print(f'Table {table} is already loaded')

        else:
            Logic_eval.tables[table] = df
            print(f"Table '{table}' was successfully loaded")

    @staticmethod
    def show(args):

        try:
            table = args['Table']
        except KeyError:
            raise KeyError('Table value was not found')

        if table in Logic_eval.tables:
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            print(Logic_eval.tables[table])
        else:
            print(f'Please load table {table} first!!')

    @staticmethod
    def create(args):

        try:
            table = args['Table']
            csvname = table + '.csv'
            argument = args['Argument']

        except KeyError:
            raise KeyError('Something went wrong')

        content = []
        header = argument

        if table in Logic_eval.tables.keys():
            print(f'There is a table already created with the name {table}')

        else:
            data = pd.DataFrame(content, columns=header)
            data.to_csv(csvname, index=False)
            Logic_eval.tables[table] = data

    @staticmethod
    def drop(args):

        try:
            table = args['Table']
        except KeyError:
            raise KeyError('Something went wrong')

        file = table + '.csv'

        if table in Logic_eval.tables.keys():
            if os.path.exists(file) and os.path.isfile(file):
                os.remove(file)
                print("file deleted")
            else:
                print("file not found")
        else:
            print(f'Please load table {table} first!!')

    @staticmethod
    def comment(args):

        try:
            table = args['Table']
            comment = args['comment']
            csvname = table + '.csv'
        except KeyError:
            raise KeyError('Something went wrong')

        if table in Logic_eval.tables.keys():
            try:
                with open(csvname, 'a', newline='') as csvfile:
                    csvfile.writelines(comment)
                    print('done')
            except KeyError:
                raise KeyError('Unable to insert comment')

        else:
            print(f'Please load table {table} first!!')

    @staticmethod
    def save(args):

        try:
            table = args['Table']
            newname = args['New_name']
            csvoldname = table + '.csv'

        except KeyError:
            raise KeyError('Something went wrong')

        if table in Logic_eval.tables.keys():
            os.rename(csvoldname, newname)
            print(f'Table {table} was saved!!')

        else:
            print(f'Please load table {table} first!!')

    @staticmethod
    def alter(args): # !DROP COLUMN doesnt work

        try:
            dropadd = args['WHAT']
            table = args['Table']
            newcolumn = args['newcolumn']
            csvname = table + '.csv'
        except KeyError:
            raise KeyError('Something went wrong')

        if table in Logic_eval.tables.keys():

        # if dropadd == "ADD":
            try:
                df = pd.read_csv(csvname)
                list_of_columns = []

                for row in df:
                    list_of_columns.append(row)

                    if newcolumn in list_of_columns:
                        print('Column exists already')
                    else:
                        df[newcolumn] = ""
                        df.to_csv(csvname, index=False)
            except KeyError:
                raise KeyError('Column already exists')

        else:
            print(f'Please load table {table} first!!')

        # if dropadd == "DROP" :
        # try:
        #     df = pd.read_csv(csvname)
        #     df.head(5)
        #     df.drop(newcolumn, axis=1, inplace=True)
        # except KeyError:
        #     raise KeyError('SOMETHING WENT WRONG')

    @staticmethod
    def procedure(args): # !Doesnt work
        try:
            command = args['Commands']
            functionprocedure = args['function']
        except KeyError:
            raise KeyError('Something went wrong')

        if functionprocedure == "SHOW":
            Logic_eval.show(command)
        if functionprocedure == "LOAD":
            Logic_eval.load(command)

    @staticmethod
    def select(args): # *WORKS WITHOUT ANY COMPARISON, ONLY 1 COLUMN
        try:
            table = args['Table']
            column = args['Column']
            csv = table + '.csv'
        except KeyError:
            raise KeyError('Something went wrong')

        if table in Logic_eval.tables.keys():
            try:
                df = pd.read_csv(csv)
                if column in df.columns:
                    print('Column exist')
                    print(df[column])
                else :
                    print('Column doesnt exist try again')
            except KeyError:
                raise KeyError('LOAD TABLE FIRST PLEASE')
        else:
            print(f'Please load table {table} first!!')

    @staticmethod
    def evaluate(ast):
        if type(ast) in (bool, float, str):
            return ast
        if type(ast) is dict:
            return Logic_eval.eval_function(ast)
        if type(ast) is list:
            ans = None
            for a in ast:
                ans = Logic_eval.evaluate(a)
            return ans

        raise Exception("Unknown AST type")

    @staticmethod
    def eval_function(ast):

        if 'function' in ast:
            function = ast["function"]

            args = ast['args']
            if function in Logic_eval.op:
                func = Logic_eval.op[function]
                return func(args)
            else:
                raise Exception(f"Unknown operator {function}")

        raise Exception('Undefined AST')
