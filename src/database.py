
import typing
import psycopg2 as pg
import model

DSN = "postgres://invest_crm:fdc804cd@localhost:5433/invest_crm?sslmode=disable"

connection = pg.connect(DSN)

def execute_raw_sql(sql):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)

def project_from_tuple(data: tuple[typing.Any, ...]):
        project = model.Project()
        project.id               = data[0]
        project.user_id          = data[1]
        project.owner_id         = data[2]
        project.address_id       = data[3]
        project.industry_id      = data[4]
        project.name             = data[5]
        project.app_own_amount   = data[6]
        project.app_sup_amount   = data[7]
        project.work_place_count = data[8]
        project.tax_amount       = data[9]
        project.desk             = data[10]
        return project

def get_all_projects() -> list[model.Project]:
    result_set: list[model.Project] = [] 
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM projects")
            for row in cursor:
                result_set.append(project_from_tuple(row))
    return result_set

def get_project(id: int) -> model.Project|None:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM projects WHERE id = %d LIMIT 1", (id,))
            data = cursor.fetchone()
            if data is None:
                return None
            return project_from_tuple(data)

def add_project(project: model.Project) -> int:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                INSERT INTO project (
                    user_id,
                    owner_id,
                    address_id,
                    industry_id,
                    name,
                    app_own_amount,
                    app_sup_amount,
                    work_place_count,
                    tax_amount,
                    desk
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''',
                (
                    project.user_id,
                    project.owner_id,
                    project.address_id,
                    project.industry_id,
                    project.app_sup_amount,
                    project.name,
                    project.app_own_amount,
                    project.app_sup_amount,
                    project.work_place_count,
                    project.tax_amount,
                )
            )
            data = cursor.fetchone()
            print(data)
            assert(not(data is None))
            a:int = data[0]
            return a
            
