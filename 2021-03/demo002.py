sql = """
INSERT INTO `pt_edu3`.`dim_resource` ( 
`title`, `desc`,
`cover_url`, 
`video_url`,
`courseware_url`, 
`courseware_pdf_url`, 
`lesson_plan_pdf_url`, `materials_pdf_url`)
VALUES
('%s', '%s', 
'https://port-release-1255999742.file.myqcloud.com/teach/G-A1/cover/%s.png',
NULL,
'https://port-release-1255999742.file.myqcloud.com/teach/G-A1/courseware/%s.pptx', 
'https://port-release-1255999742.file.myqcloud.com/teach/G-A1/courseware_pdf/%s.pdf', 
NULL, NULL);
"""

names = ['动手搭建第一个小程序', '小车跑起来', '轮子转起来', '声音响起来', '月下景色', '诗人吟诗', '我会玩编程']
sql2 = """INSERT INTO `pt_edu3`.`dim_point` ( `id`, `name`, `father_id`, `lang_type`, `series_id`, `resource_id`, `sort`, `create_time`, `update_time` )VALUES( 1160, '%s', 1157, 2, 35, 8478, 5, NOW(), NOW());"""
for i in names:
    print(sql2 % (i, ))
