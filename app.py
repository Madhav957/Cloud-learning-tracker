from flask import Flask, request, jsonify
from db import db
from skills import bp as skills_bp

app = Flask(__name__)

app.register_blueprint(skills_bp)

@app.route("/")
def greet():
   return "Hello User"

@app.route("/users", methods = ["POST"])
def create_user():
     data = request.get_json()

     username = data["username"]
     email = data["email"]

     cursor = db.cursor()
     query = """
     INSERT INTO users(username,email)
     VALUES(%s, %s)
     """
     cursor.execute(query,(username,email))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "User Created Successfully !"
     }),201



@app.route("/users",methods=["GET"])
def get_users():
     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM users"
     cursor.execute(query)
     users = cursor.fetchall()
     cursor.close()
     return jsonify(users)

@app.route("/users/<userid>", methods = ["GET"])
def get_user(userid):
     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM users WHERE userid = %s"
     cursor.execute(query,(userid,))
     user = cursor.fetchone()
     cursor.close()
     return jsonify(user)

@app.route("/users/<userid>",methods=["PUT"])
def update_user(userid):
     data = request.get_json()
     username = data["username"]
     email = data["email"]
     cursor = db.cursor()
     query = "UPDATE users SET username = %s , email = %s WHERE userid = %s"
     cursor.execute(query,(username,email,userid))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "Data Updated !"
     })

@app.route("/users/<userid>", methods = ["DELETE"])
def delete_user(userid):
     cursor = db.cursor()
     query = "DELETE FROM users WHERE userid = %s"
     cursor.execute(query,(userid,))
     db.commit()
     cursor.close()
     return jsonify(userid)

################################ END OF USERS ################################
# DATE : 23/08/2026
@app.route("/courses",methods = ["POST"])
def create_course():
     data = request.get_json()
     coursename = data["coursename"]
     provider = data["provider"]
     category = data["category"]
     current_progress = data["current_progress"]
     status = data["status"]
     start_date = data["start_date"]
     userid = data["userid"]
     cursor = db.cursor()
     query = """
     INSERT INTO courses(
     coursename,
     provider,
     category,
     current_progress,
     status,
     start_date,
     userid
     )
     VALUES(%s, %s, %s, %s, %s, %s, %s);
     """
     cursor.execute(query,(coursename,provider,category,current_progress,status,start_date,userid))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "Course Created !"
     }),201


@app.route("/users/<userid>/courses", methods=["GET"])
def get_courses(userid):
     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM courses WHERE userid = %s"
     cursor.execute(query,(userid,))
     courses = cursor.fetchall()
     cursor.close()
     return jsonify(courses)

@app.route("/courses/<courseid>", methods = ["GET"])
def get_course(courseid):
     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM courses WHERE courseid = %s"
     cursor.execute(query,(courseid,))
     courses = cursor.fetchone()
     cursor.close()
     return jsonify(courses)

@app.route("/courses/<courseid>",methods = ["PUT"])
def update_courses(courseid):
     cursor =  db.cursor()
     data = request.get_json()
     coursename = data["coursename"]
     provider = data["provider"]
     category = data["category"]
     current_progress = data["current_progress"]
     status = data["status"]
     start_date = data["start_date"]
     query = "UPDATE courses SET coursename = %s, provider = %s, category = %s, current_progress = %s, status = %s,start_date = %s WHERE courseid = %s"
     cursor.execute(query,(coursename,provider,category,current_progress,status,start_date,courseid))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "Courses Updated !"
     }),200

@app.route("/courses/<courseid>",methods = ["DELETE"])
def delete_course(courseid):
     cursor = db.cursor()
     query  = "DELETE FROM courses where courseid = %s"
     cursor.execute(query,(courseid,))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "Course Deleted !"
     }),200


################################ END OF COURSES ################################
# DATE : 24/08/26
@app.route("/projects",methods=["POST"])
def create_project():
     data = request.get_json()
     project_name = data["project_name"]
     description = data["description"]
     technologies_used = data["technologies_used"]
     status = data["status"]
     start_date = data["start_date"]
     complete_date = data["complete_date"]
     userid = data["userid"]
     cursor = db.cursor()
     query = """
     INSERT INTO projects (
     project_name,
     description,
     technologies_used,
     status,
     start_date,
     complete_date,
     userid
     )
     values ( %s,%s,%s,%s,%s,%s,%s)
     """
     cursor.execute(query,(project_name,description,technologies_used,status,start_date,complete_date,userid))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "Project created !"
     }),201

@app.route("/users/<userid>/projects",methods = ["GET"])
def get_projects(userid):

     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM projects WHERE userid = %s"
     cursor.execute(query,(userid,))
     projects = cursor.fetchall()
     cursor.close()
     return jsonify(projects)


@app.route("/projects/<projectid>",methods = ["GET"])
def get_project(projectid):
     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM projects WHERE projectid = %s"
     cursor.execute(query,(projectid,))
     projects = cursor.fetchone()
     cursor.close()
     return jsonify(projects)

@app.route("/projects/<projectid>",methods = ["PUT"])
def update_project(projectid):
     data = request.get_json()
     project_name = data["project_name"]
     description = data["description"]
     technologies_used = data["technologies_used"]
     status = data["status"]
     start_date = data["start_date"]
     complete_date = data["complete_date"]
     cursor = db.cursor()
     query = "UPDATE projects SET project_name = %s, description = %s, technologies_used = %s, status = %s,start_date = %s,complete_date= %s WHERE projectid = %s"
     cursor.execute(query,(project_name,description,technologies_used,status,start_date,complete_date,projectid))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "Projects updated !"
     })

@app.route("/projects/<projectid>", methods=["DELETE"])
def delete_project(projectid):
    cursor = db.cursor()

    query = "DELETE FROM projects WHERE projectid = %s"

    cursor.execute(query, (projectid,))

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Project deleted!"
    })

#DATE : 25/08/26

@app.route("/certifications", methods=["POST"])
def create_certification():
     data = request.get_json()
     certification_name = data["certification_name"]
     provider = data["provider"]
     category = data["category"]
     issue_date = data["issue_date"]
     expiry_date = data["expiry_date"]
     credential_url = data["credential_url"]
     userid = data["userid"]
     cursor = db.cursor()
     query = """
     INSERT INTO certifications(certification_name,provider,category,issue_date,expiry_date,credential_url,userid)
     values(%s, %s, %s,%s,%s,%s,%s)
     """
     cursor.execute(query, (
     certification_name,
     provider,
     category,
     issue_date,
     expiry_date,
     credential_url,
     userid
     ))
     db.commit()
     cursor.close()
     return jsonify({
          "message" : "Certificate Created !"
     }),201

@app.route("/users/<userid>/certifications",methods = ["GET"])
def get_certifications(userid):
     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM certifications WHERE userid = %s"
     cursor.execute(query,(userid,))
     certifications = cursor.fetchall()
     cursor.close()
     return jsonify(certifications)

@app.route("/certifications/<certid>",methods = ["GET"])
def get_certification(certid):
     cursor = db.cursor(dictionary=True)
     query = "SELECT * FROM certifications WHERE certid = %s"
     cursor.execute(query,(certid,))
     certifications = cursor.fetchone()
     cursor.close()
     return jsonify(certifications)

@app.route("/certifications/<certid>", methods=["PUT"])
def update_certification(certid):

    data = request.get_json()

    certification_name = data["certification_name"]
    provider = data["provider"]
    category = data["category"]
    issue_date = data["issue_date"]
    expiry_date = data["expiry_date"]
    credential_url = data["credential_url"]

    cursor = db.cursor()

    query = """
    UPDATE certifications
    SET certification_name = %s,
        provider = %s,
        category = %s,
        issue_date = %s,
        expiry_date = %s,
        credential_url = %s
    WHERE certid = %s
    """

    cursor.execute(
        query,
        (
            certification_name,
            provider,
            category,
            issue_date,
            expiry_date,
            credential_url,
            certid
        )
    )

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Certification updated!"
    })

@app.route("/certifications/<certid>", methods=["DELETE"])
def delete_certification(certid):

    cursor = db.cursor()

    query = "DELETE FROM certifications WHERE certid = %s"

    cursor.execute(query, (certid,))

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Certification deleted!"
    })




if __name__ == "__main__":
      app.run(debug=True)

 


