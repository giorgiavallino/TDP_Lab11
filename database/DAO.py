from database.DB_connect import DBConnect

class DAO():

    def __init__(self):
        pass

    @staticmethod
    def getAllColours():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select distinct(gp.Product_color )
                from go_products gp
                order by gp.Product_color """
        cursor.execute(query,)
        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        conn.close()
        return result