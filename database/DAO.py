from database.DB_connect import DBConnect
class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getNodi(annoI, annoF):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.*
                from constructors c ,results r ,races r2 
                where r2.`year` between %s and %s and r.raceId =r2.raceId and r.constructorId =c.constructorId and r.`position` is not null """

        cursor.execute(query, (annoI, annoF))

        for row in cursor:
            results.append(Costruttore(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getArchi(annoI, annoF, idMapA):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select c1.constructorId as co1, c2.constructorId as co2,count (distinct c1.driverId) as peso
            from (select distinct c.constructorId,r.driverId,r2.raceId
            from constructors c ,results r ,races r2 
            where r2.`year` between %s and %s and r.raceId =r2.raceId and r.constructorId =c.constructorId and r.`position` is not null 
        )c1, (select distinct c.constructorId,r.driverId,r2.raceId
            from constructors c ,results r ,races r2 
        where r2.`year` between %s and %s and r.raceId =r2.raceId and r.constructorId =c.constructorId and r.`position` is not null 
            )c2
    where c1.constructorId<c2.constructorId and c1.driverId=c2.driverId and c1.raceId<>c2.raceId
    group by c1.constructorId,c2.constructorId
"""

        cursor.execute(query, (annoI, annoF, annoI,annoF,))

        for row in cursor:
            results.append(Arco(idMapA[row["co1"]], idMapA[row["co2"]], row["peso"]))

        cursor.close()
        conn.close()
        return results

