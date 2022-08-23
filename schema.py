from app import d

class Students(d.Model):
    student_id = d.Column(d.Integer,nullable=False,primary_key=True)
    email = d.Column(d.String(100),nullable=False)
    country = d.Column(d.String(100),nullable=False)
    native_language = d.Column(d.String(20),nullable=True)
    telephon = (d.Integer,nullable=False,primary_key=True)

class Foreign_language(d.Model):
    language_id = d.Column(d.Integer,nullable=False,primary_key=True)
    language_name = d.Column(d.String(100),nullable=False)
    student_id = d.Column(d.Integer,d.ForeignKey('colleges.college_id'),nullable=False)