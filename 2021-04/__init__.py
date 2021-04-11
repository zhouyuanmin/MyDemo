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
print(len(subject_ids))
user_ids = [873,
            1150,
            1162,
            1152,
            1159,
            543,
            252,
            1182,
            1157,
            1156,
            762,
            1173,
            1175,
            535,
            1170,
            1149,
            1167,
            1161,
            1155,
            622,
            1172,
            1160,
            1177,
            1178,
            459,
            1174,
            1183,
            1153,
            478,
            1165,
            1166,
            1163,
            1151,
            1169,
            1168,
            1180,
            1154,
            171,
            1164,
            1181,
            1176,
            1171]
print(len(user_ids))
sql = """INSERT INTO `pt_exam`.`user_paper_record` (`exam_id`, `room_id`, `paper_id`, `user_id`, `subject_id`) VALUES (19, 22, 14, %s, %s);"""

sql_user_paper = """INSERT INTO `pt_exam`.`user_paper` (`exam_id`, `room_id`, `paper_id`, `user_id`, `grade`, `create_time`, `start_do_time`, `submit_time`, `flag`, `awarded`) VALUES (19, 22, 14, %s, 0, now(), NULL, NULL, 0, 0);"""

for uid in user_ids:
    print(sql_user_paper % (uid,))

sql_user_exam = """INSERT INTO `pt_exam`.`user_exam` (`exam_id`, `user_id`, `room_id`, `step`, `id_photo_url`, `ticket_no`, `ticket_url`, `level`, `flag`, `certificate_url`, `certificate_no`, `create_time`, `resit_flag`) VALUES (19, %s, 22, 2, NULL, '学号先填为null，后面执行脚本赋值', NULL, NULL, 0, NULL, NULL, now(), 0);"""
"""UPDATE `pt_exam`.`user_exam` SET `ticket_no` = '51013698231948' WHERE `user_id` = 1157 AND exam_id=19;"""
for uid in user_ids:
    print(sql_user_exam % (uid,))

for uid in user_ids:
    for sid in subject_ids:
        print(sql % (uid, sid))
