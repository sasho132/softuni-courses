class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def __search_by_id(self, entities, entity_id):
        return [e for e in entities if e.id == entity_id][0]

    def edit_category(self, category_id, new_name):
        category = self.__search_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__search_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.__search_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__search_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__search_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__search_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__search_by_id(self.documents, document_id)
        return document

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += f"{document}"
        return result
