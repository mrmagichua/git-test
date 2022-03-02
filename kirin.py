import flask

app = flask.Flask(__name__) #初始化app对象，当前模块名称name

@app.route("/hello")#告诉服务器你的url地址
def hello():
    return "hello flask"
    #git2
    #git3
    #git4
    #git5 - master



@app.route("/get_grades")
def get_grades():
    grades = []
    with open("input.txt") as fin:
        for line in fin:
            line = line.strip()
            fields = line.split("\t")
            grades.append(fields)
    import json
    return json.dumps(grades) #返回json的字符串

@app.route("/get_grades_byid/<sid>")#设置id查找成绩
def get_grades_byid(sid):#参数给到func
    grades = []
    with open("input.txt") as fin:
        for line in fin:
            line = line.strip()
            fields = line.split("\t")
            if str(sid) == fields[0]:
                grades.append(fields)

    import json
    return json.dumps(grades) #返回json的字符串

app.run()