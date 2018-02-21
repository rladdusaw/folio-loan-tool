from request_service import RequestService

class Inventory(object):
    """Wrapper for the FOLIO inventory API"""

    def __init__(self, session):
        self.session = session
        self.rs = RequestService(self.session)

    def get_items(self):
        """Retrieves items
        Query Parameters
            query: JOSN array (optional)
            offset: integer (default=0)
            limit: integer (default=10)
            lang: string (default=en)
        """
        pass

    def post_items(self):
        pass

    def delete_items(self):
        pass

    def get_items_by_item_id(self):
        pass

    def delete_items_by_item_id(self):
        pass

    def put_items_by_item_id(self):
        pass

    def get_instances(self):
        pass

    def post_instances(self):
        pass

    def delete_instances(self):
        pass

    def get_instances_by_instance_id(self):
        pass

    def delete_instances_by_instance_id(self):
        pass

    def put_instances_by_instance_id(self):
        pass

    def get_instances_context(self):
        pass

    def post_ingest_mods(self):
        pass

    def get_ingest_mods_status_by_id(self):
        pass