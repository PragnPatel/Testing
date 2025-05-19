# import multiprocessing
# import time

# def square():
#     for i in range(1,10):
#         time.sleep(1)
#         print(f"square: {i*i}")
        
# def cube():
#     for i in range(1,10):
#         time.sleep(1.5)
#         print(f"cube: {i*i*i}")

# if __name__ == "__main__":


#     p1=multiprocessing.Process(target=square)
#     p2=multiprocessing.Process(target=cube)

#     t=time.time()
#     # square()
#     # cube()
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()


#     print(time.time()-t)


from concurrent.futures import ProcessPoolExecutor
import time

def number(n):
    time.sleep(2)
    return f"number: {n}"
numbers=[1,2,3,4,5,65,7,87,89,9,9,8,7,7,4,4,5,5,7,8,8,6,5,4,3,2]
t=time.time()

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=50) as executor:
        result = executor.map(number,numbers)

    for r in result:
        print(r)

    print(time.time()-t)