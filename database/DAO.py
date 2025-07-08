from database.DB_connect import DBConnect
from model.go_products import Go_products

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

    @staticmethod
    def getAllProductsByColour(colore):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select *
                from go_products gp
                where gp.Product_color = %s"""
        cursor.execute(query, (colore,))
        for row in cursor:
            result.append(Go_products(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdge(colore, anno, prodotto_01, prodotto_02):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT t3.P1, t3.P2, COUNT(*) AS peso
                FROM
                (SELECT t1.Retailer_code, t1.Product_number AS P1, t2.Product_number AS P2, t1.`Date` 
                FROM (
                SELECT gds1.Retailer_code, gds1.Product_number, gds1.`Date` 
                FROM go_daily_sales gds1 , go_products gp1
                WHERE gds1.Product_number = gp1.Product_number AND gds1.Product_number = %s
                AND gp1.Product_color = %s AND YEAR(gds1.`Date`) = %s
                ) t1
                INNER JOIN (
                SELECT gds2.Retailer_code, gds2.Product_number, gds2.`Date`
                FROM go_daily_sales gds2, go_products gp2  
                WHERE gds2.Product_number = gp2.Product_number AND gds2.Product_number = %s 
                AND gp2.Product_color = %s AND YEAR(gds2.`Date`) = %s
                ) t2 
                ON t1.`Date` = t2.`Date` AND t1.Retailer_code = t2.Retailer_code
                GROUP BY t1.`Date`) t3"""
        cursor.execute(query, (prodotto_01, colore, anno, prodotto_02, colore, anno,))
        row = cursor.fetchone()
        tuplaArco = (row["P1"], row["P2"], row["peso"])
        cursor.close()
        conn.close()
        return tuplaArco