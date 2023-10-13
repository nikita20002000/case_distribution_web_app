# Created by nikitanovikov at 11.10.2023

# Приложение для расчета показателей компании
# Приложение для оптимизации работы компании в условиях ковид


###________________________БИБЛИОТЕКИ___________________________###
import os
import time
import asyncio
import pandas as super_puper_lib
import matplotlib.pyplot as plt
import pywebio
from pywebio import start_server
from pywebio.input import input, input_group
from pywebio.pin import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js
import re
###_____________________________________________________________###

# Прописываем пути к файлам
logo_path = os.path.join('data', 'my_logo.png')
office_plan_first = os.path.join('data', 'office_plan.png')
office_path_final = os.path.join('data', 'office_final_plan.png')
table_1 = os.path.join('data', '1_table.csv')



db = super_puper_lib.read_csv(table_1)



pywebio.config(theme='dark')


def alg(p):
    max_workers = int(p.input)
    places_array = map(int, (p.input2.split(',')))

    final_list = []
    i = 0

    for place in places_array:
        counter = 0
        coef = 0
        i = 0
        while round(i, 1) >= 3.6 or i == 0 and max_workers != 0:
            counter += 1
            max_workers -= 1
            i = place / counter

        final_list.append(f'{counter} человек - {place} м²')

    return put_text(f'Текущее распредление по кабинетам: {final_list}  \nКоличество сотрудников, которые не попали в офис - {max_workers}')



def main():
    # logo_path = os.path.join('data', 'my_logo.png')

    put_image(open(logo_path, 'rb').read(), width='200px').style("display: block;"
                                                                 "margin-left: auto;"
                                                                 "margin-right: auto ")

    put_button("Подробнее", onclick=lambda: popup('Подробнее', [
                                    put_text('Данное приложение было создано в рамках решения кейса "Офис без границ", любое его использование в коммерчесских целях будет преследоваться по закону и лично создателем приложения!\n'
                                             '😎'),
                                    put_buttons(['Закрыть'], onclick=lambda _: close_popup())
                                    ]), color='info', outline=True).style(f"float:right;"
                                                                "margin: 0px 0px 0px 15px;")

    put_html('<h1>'
                'Приложение для оптимизации рабочего места в офисах компаний'
             '</h1>'
             )

    put_text('Ниже представлена таблица данных по офисам компании в различных городах')
    put_html(db.to_html(border=1)).style('width: 1000px'
                                         'margin: 0 auto;')
    put_text('\n\n\n')
    put_text(''
             'Кликни ниже, чтобы увидеть подробнее')
    def btn_click(btn_val):
        with use_scope('A'):
            match btn_val:
                case 'Версия офиса без оптимизации':
                    clear('A')
                    put_text(
                        'Вот пример плана офиса компании, на рисунке отчетливо видно, что количество сотрудников на квадратный метр сильно превышено и требует оптимизации!\n\n'
                        )
                    put_image(open(office_plan_first, 'rb').read(), width='1000px').style("display: block;"
                                                                 "margin-left: auto;"
                                                                 "margin-right: auto ")
                case 'Новая оптимизированная версия':
                    clear('A')
                    put_text(
                        'Произошла магия! Теперь количество сотрудников на площади соответствует нормам!\n\n'
                    )
                    put_image(open(office_path_final, 'rb').read(), width='1000px').style("display: block;"
                                                                     "margin-left: auto;"
                                                                   "margin-right: auto ")
                    put_text('\n')
                    put_collapse('Посмотреть алгоритм оптимизации',
                        put_code(content="import java.util.ArrayList;\n"
                                         "import java.util.List;\n\n"
                                         "public class Main {\n\n"
                                         "\tpublic static void main(String[] args) {\n"
                                         "\t\tint max_workers = 599;\n"
                                         "\t\tint distant_workers = (int) (599 * 15 / 100);\n"
                                         "\t\tint[] places_array = {46, 70, 15, 112, 99, 75, 68, 28, 99, 448, 62, 83, 166, 378};\n"
                                         "\t\tList<String> final_list = new ArrayList<>();\n\n"
                                         "\t\tint counter;\n"
                                         "\t\tdouble coef;\n"
                                         "\t\tint i;\n\n"
                                         "\t\tfor (int place : places_array) {\n"
                                         "\t\t\tcounter = 0;\n"
                                         "\t\t\tcoef = 0;\n"
                                         "\t\t\ti = 0;\n\n"
                                         "\t\t\twhile (Math.round(i * 10) / 10.0 >= 3.6 || i == 0 && max_workers != 0) {\n"
                                         "\t\t\t\tcounter += 1;\n"
                                         "\t\t\t\tmax_workers -= 1;\n"
                                         "\t\t\t\ti = place / counter;\n"
                                         "\t\t\t}\n\n"
                                         "\t\t\tfinal_list.add(counter + ' - ' + place);\n"
                                         "\t\t}\n"
                                         "\tSystem.out.println(final_list);\n"
                                         "\t}\n"
                                         "}", language='java'))
                    put_text('\n\n')
                    put_html('<h2>'
                             'Попробовать алгоритм'
                             '</h2>'
                             '<p>'
                             'Здесь вы можете попробовать алгоритм расчета рабочего пространства для нужд вашей компании'
                             '</p>', position=-1
                             )



                    put_input('input', label='Введите суммарное офисное пространство в м²')
                    put_input('input2', label='Введите площадь кабинетов через запятую\n (Пример: 12,4,15)')

                    put_buttons(['Get FINAL Value'], lambda _: alg(pin))










    put_buttons(['Версия офиса без оптимизации', 'Новая оптимизированная версия'], onclick=btn_click)







if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False, remote_access=True)