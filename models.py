from sqlalchemy import column,Integer,String,Boolean

class ToDo():
    __tablename__ = "todos"

    id = column(Integer,primary_key = True, index = True)
    title = column(String,index=True)
    description = column(String , nullable = False)
    done = column(Boolean,default = False)