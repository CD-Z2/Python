import redis


def make_input():
    num = 0
    try:
        num = int(input("Enter the index of a Fibonacci number:"))
    except:
        make_input()
    if num < 0:
        num = 0
    return num


def get_fibonacci(number):
    global fibonacci
    for x in range(2, number + 1):
        fibonacci = fibonacci + [fibonacci[x - 2] + fibonacci[x - 1]]
    return fibonacci[number]


fibonacci = [0, 1]
r = redis.StrictRedis(host='10.115.2.20', port=6379, db=0, charset='utf-8', decode_responses=True)

wanted_num = make_input()
print(get_fibonacci(wanted_num))

for i in range(wanted_num + 1):
    r.set(f"f-{i}", fibonacci[i])
