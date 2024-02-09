import numpy as np
import math
import random

def sred_time_EVM(kol):
    summ=0
    iznach_kol=kol
    while(kol>0):
        summ+=random.choice([10, 23])
        kol-=1
    return summ/iznach_kol

def modelling(registration_time, error_probability, count_task, time_enter, error_time, processing_time):
    count_task=count_task-1
    error_counter = 0

    workload_first_evm = 1
    workload_second_evm = 0

    count_first = 0
    count_second = 0

    counter = 1
    queue_on_hold = 1

    time_work_first_evm = 0
    time_work_second_evm = 0
    time_registration = registration_time
    time_error_complete = 0

    while counter <= count_task and queue_on_hold:
        if (counter + registration_time // time_enter > count_task) and counter < count_task:
            differ = count_task - counter
            counter += differ
            queue_on_hold += differ

        elif counter < count_task:
            counter += registration_time // time_enter
            queue_on_hold += registration_time // time_enter
        if queue_on_hold != 0:
            queue_on_hold -= 1
            if time_work_first_evm<time_work_second_evm:
                workload_first_evm += 1
            else:
                workload_second_evm += 1
            time_registration += registration_time
#####
        if workload_first_evm != 0:
            count_first += 1
            time_work_first_evm += processing_time
            if random.random() < error_probability:
                time_error_complete += error_time
                error_counter += 1
                time_work_first_evm += processing_time + error_time
                workload_first_evm -= 1
            else:
                workload_first_evm -= 1

        if workload_second_evm != 0:
            count_second += 1
            time_work_second_evm += processing_time
            if random.random() < error_probability:
                time_error_complete += error_time
                error_counter += 1
                time_work_second_evm += processing_time+error_time
                workload_second_evm -= 1
            else:
                workload_second_evm -= 1


    print('\nДлина очереди: ',registration_time//time_enter)
    print('\nКоличество выполненных заданий', counter+1)
    print('Количество вызванных ошибок', error_counter)
    print('Времени затрачено на регистрацию:', round(time_registration / 60, 2), 'ч.')
    print('Времени затрачено на исправлении ошибки:', round(time_error_complete / 60, 2), 'ч.')
    if time_work_first_evm> time_work_second_evm:
        prostoi = time_registration - time_work_first_evm
    else: prostoi = time_registration - time_work_second_evm
    print('Cреденее время пребывания в сиситеме:',
          round(((time_work_first_evm + time_work_second_evm + prostoi) / count_task) / 60, 2), 'ч.')
    print('Cреденее время выполнения заявки:',
          round(((time_work_first_evm + time_work_second_evm) / count_task) / 60, 2), 'ч.')

    print('Количество выполненных заданий на первой ЭВМ:', count_first)
    print('Количество выполненных заданий на второй ЭВМ:', count_second)
    print('Время работы первой ЭВМ:', round(time_work_first_evm / 60, 2), 'ч.')
    print('Время работы второй ЭВМ:', round(time_work_second_evm / 60, 2), 'ч.')
    all_time=0
    if time_registration>max(time_work_first_evm,time_work_second_evm):
        all_time=round((time_registration+random.choice([10, 23])) / 60,2)  # !!!!! заменить цифры на переменные
    else:
        all_time=max(time_work_first_evm,time_work_second_evm)+registration_time
    print('Общее время:',all_time, 'ч.')

    # счет ИНТЕНСИВНОСТИ НАГРУЗКИ
    a = registration_time + error_time + processing_time
    b = round((1 - error_probability), 2)
    print('ИНТЕНСИВНОСТЬ НАГРУЗКИ(ро) ф-ла:',
          round(((error_probability * a + b * processing_time) / registration_time), 2))

    print('ПРОПУСКНАЯ СПОСОБНОСТЬ', round((count_task / all_time), 2), " задач/ч")

    # Cреденее время нахождения в очереди
    lamda = 1 / time_enter
    mu = 1 / processing_time
    v_ocheredi = lamda / (mu * abs(mu - lamda))
    print('Cреденее время нахождения в очереди:', round(v_ocheredi/60, 2), ' ч')

    igig = time_registration + random.choice([10, 23])
    print('Время обработки всех 100 заданий:', round(igig / 60, 2), ' ч')

    print('средние число каналов под обслуживанием ф-ла', round((1 + 2 + 2) / 3, 2), 'каналов')

    print('Общее количество деталей в очереди',all_time*60/2)


def main():
    print("Данные хотите ввести или использовать по условию?")
    ans = input("ввести или не ввести\ny/n\n")
    if (ans == "n"):
        registration_time = 12
        error_probability = 0.7
        count_task = 100
        time_enter = 2
        error_time = 3
        processing_time = 10
        modelling(registration_time, error_probability, count_task, time_enter, error_time, processing_time)
    else:
        registration_time = int(input("введите время регистрации: "))
        error_probability = int(input("сколько в процентах обработки заданий произойдет ошибка?: ")) / 100
        count_task = int(input("количество заданий: "))
        time_enter = int(input("задания на обработку поступают каждые: "))
        error_time = int(input("время на повторною обработку: "))
        processing_time = int(input("время на обработку данных: "))
        modelling(registration_time, error_probability, count_task, time_enter, error_time, processing_time)


if __name__ == '__main__':
    main()