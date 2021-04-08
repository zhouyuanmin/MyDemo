subject_ids = [847,
               848,
               849,
               850,
               851,
               852,
               853,
               854,
               855,
               856,
               857,
               858,
               859,
               860,
               861,
               862,
               863,
               864,
               865,
               866,
               867,
               868,
               869,
               870,
               871,
               9722,
               9723,
               9724,
               9725,
               9726,
               9727,
               9728]

user_ids = [960]

sql = """INSERT INTO `pt_exam`.`user_paper_record` (`exam_id`, `room_id`, `paper_id`, `user_id`, `subject_id`) VALUES (18, 21, 14,%s, %s);"""

for uid in user_ids:
    for sid in subject_ids:
        print(sql % (uid, sid))
