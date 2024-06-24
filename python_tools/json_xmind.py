import xmind
import json

def xmind_to_json(xmind_file_path, json_file_path):
    # 加载XMind文件
    workbook = xmind.load(xmind_file_path)
    sheet = workbook.getPrimarySheet()
    root_topic = sheet.getRootTopic()

    # 将XMind内容转换为JSON
    json_data = traverse_topic(root_topic)

    # 将JSON数据写入文件
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=2, sort_keys=True)

def traverse_topic(topic):
    topic_data = {
        'title': topic.getTitle(),
        'topics': []
    }

    # 处理子主题
    subtopics = topic.getSubTopics()
    for subtopic in subtopics:
        subtopic_data = traverse_topic(subtopic)
        topic_data['topics'].append(subtopic_data)

    return topic_data



if __name__ == '__main__':

    # 使用示例
    xmind_file = r'C:\Users\EDY\Desktop\test/test.xmind'
    json_file = r'C:\Users\EDY\Desktop\test/test.json'
    xmind_to_json(xmind_file, json_file)
