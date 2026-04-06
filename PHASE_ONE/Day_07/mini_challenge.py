# In this program we will try to solve a mini challenge

# "Smart Course Enrollment Checker"

#Build a program that prints:

#╔══════════════════════════════════════════╗
#      📚 COURSE ENROLLMENT ANALYSIS
#╠══════════════════════════════════════════╣
#  Total Courses Available  : 8

 # 👤 ALI
  #   Enrolled In  : CS101, CS201, ENG101, MATH201
   #  Not Enrolled : CS301, ENG201, MATH301, PHY101

  #👤 SARA
   #  Enrolled In  : CS101, CS301, MATH201, PHY101
    # Not Enrolled : CS201, ENG101, ENG201, MATH301

  #👤 FATIMA
   #  Enrolled In  : CS201, CS301, ENG201, MATH301
    # Not Enrolled : CS101, ENG101, MATH201, PHY101
#╠══════════════════════════════════════════╣
 # 🤝 Ali & Sara share     : CS101, MATH201
  #🤝 Ali & Fatima share   : CS201
  #🤝 Sara & Fatima share  : CS301
 # 🌟 All three share      : None
#╠══════════════════════════════════════════╣
 # 📊 All unique courses taken by students:
  #   CS101, CS201, CS301, ENG101, ENG201,
   #  MATH201, MATH301, PHY101
#╚══════════════════════════════════════════╝



all_courses     = {"CS101","MATH201","ENG101","PHY101",
                   "CS201","MATH301","CS301","ENG201"}

ali_courses     = {"CS101", "MATH201", "ENG101", "CS201"}
sara_courses    = {"CS101", "PHY101", "MATH201", "CS301"}
fatima_courses  = {"CS201", "CS301", "ENG201", "MATH301"}



total_courses = len(all_courses)

not_enrolled_ali = all_courses - ali_courses
not_enrolled_sara = all_courses - sara_courses
not_enrolled_fatima = all_courses - fatima_courses

ali_sara = ali_courses & sara_courses
ali_fatima = ali_courses & fatima_courses
sara_fatima = sara_courses & fatima_courses

ali_sara_fatima = ali_courses & sara_courses & fatima_courses

all_unique = ali_courses | sara_courses | fatima_courses



print(f"")
print(f"")
print(f"")
print(f"╔══════════════════════════════════════════╗")
print(f"        📚 COURSE ENROLLMENT ANALYSIS")
print(f"╠══════════════════════════════════════════╣")
print(f"Total Courses Available  : {total_courses}")
print(f"")
print(f"👤 ALI")
print(f"Enrolled In  : {ali_courses}")
print(f"Not Enrolled : {not_enrolled_ali}")
print(f"")
print(f"👤 SARA")
print(f"Enrolled In  : {sara_courses}")
print(f"Not Enrolled : {not_enrolled_sara}")
print(f"")
print(f"👤 FATIMA")
print(f"Enrolled In  : {fatima_courses}")
print(f"Not Enrolled : {not_enrolled_fatima}")
print(f"╠══════════════════════════════════════════╣")
print(f"")
print(f"🤝 Ali & Sara share     : {ali_sara}")
print(f"🤝 Ali & Fatima share   : {ali_fatima}")
print(f"🤝 Sara & Fatima share  : {sara_fatima}")
print(f"🌟 All three share      : {ali_sara_fatima}")
print(f"╠══════════════════════════════════════════╣")
print(f"")
print(f"📊 All unique courses taken by students: {all_unique}")
print(f"╚══════════════════════════════════════════╝")
print(f"")
print(f"")
print(f"")
print(f"")
