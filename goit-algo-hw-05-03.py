import sys
from collections import defaultdict
from pathlib import Path

def parse_log_line(line: str) -> dict:
    keys = ['date', 'time','level', 'mess']
    return dict(zip(keys, line.split(' ', maxsplit=3)))

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r+') as log_file:
            lines=list(filter(lambda x: x is not None,(map(parse_log_line,log_file.readlines()))))
            return lines
    except Exception as e:
        print(f"ERROR: {e}")
    
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x['level']==level,logs))

def count_logs_by_level(logs: list) -> dict:
    level_counter=defaultdict()
    level_counter.default_factory=int  
    for log in logs:
        level_counter[log['level']]+=1
    return dict(level_counter)

def display_log_counts(counts: dict):
    print(f"{'Рівень логування ':20}| Кількість ")
    print(f"{'-'*20}|{'-'*10}")
    print("\n".join(list(map(lambda x:f"{x:20}| {counts[x]}",counts))))

if __name__=="__main__":
    if  len(sys.argv) == 1:
        print(f"File path is not specified")
        exit

    filename = Path(sys.argv[1])
    if not filename.exists():
        print(f"No such file or directory: {filename}")
        exit
    
    else:          
        logs=load_logs(file_path=filename)
        display_log_counts(count_logs_by_level(logs))
        if len(sys.argv)==3:
            level=sys.argv[2]
            logs=filter_logs_by_level(logs,level)
            print()
            print(f"Деталі логів для рівня '{level}':")
            print(''.join(map(lambda x:f"{x['date']} {x['time']} - {x['mess']}",logs)))
    

