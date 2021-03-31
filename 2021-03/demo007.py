sql = """INSERT INTO `pt_edu3`.`dim_resource` (`title`, `desc`, `cover_url`, `video_url`, `courseware_url`, `courseware_pdf_url`, `lesson_plan_pdf_url`, `materials_pdf_url`, `create_time`, `update_time`) VALUES ('%s', NULL, '', NULL, 'https://port-release-1255999742.file.myqcloud.com/teach/Mr专题课程/courseware/%s.pptx', 'https://port-release-1255999742.file.myqcloud.com/teach/Mr专题课程/courseware_pdf/%s.pdf', NULL, NULL, NOW(), NOW());"""

data = ['机器人-初始机器人', '机器人-广播体操', '机器人-基础动作指令', '机器人-体操动作指令', '机器人-体操项目实现']

for d in data:
    print(sql % (d, d, d))
