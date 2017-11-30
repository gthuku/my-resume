from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    p1 = Professor(name='Amanda Convery', department='Accounting & MIS')
    p2 = Professor(name='Jackson Gillespie', department='Accounting & MIS')
    p3 = Professor(name='Vicki Cotter', department='Business Administration')
    p4 = Professor(name='Pratyush Sharma', department='Accounting & MIS')
    course1 = Course(course_number='ACCT 315', title='Intermediate Accounting I', description='In-depth coverage of financial accounting. Topics include: environment and conceptual framework of financial accounting; review of the accounting process; preparation of financial statements; recognition and measurement')
    course2 = Course(course_number='ACCT 327', title='Cost Accounting', description='Process, job order and standard costing; variable and absorption costing; budgeting, decentralization, and transfer pricing; and cost analysis for managerial applications.')
    course3 = Course(course_number='BUAD 309', title='Organizational Behavior', description='Examines individual, group, and organizational determinants of work behavior in organizations. Theory and concepts relevant to individual differences, attitudes, motivation, teams, leadership, power, and organizational culture and change are discussed with an emphasis on applying this knowledge to the challenges of management in a variety of organizations.')
    course4 = Course(course_number='MISY 330', title='Database Design and Implementation', description='Covers the design and implementation of enterprise databases in the business environment. A networked setting and its effect on database management will be emphasized.')
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
