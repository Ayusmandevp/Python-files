import logging
logging.basicConfig(filename="exceptionhandeling.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
logging.info("-------------New Run-------------")
try:
    logging.info("Taking input of number and diviser in try block")
    num=int(input("Enter a number"))
    div=int(input("Enter the diviser"))
    logging.info("printing number/diviser")
    logging.info("Number: {}, Diviser {}, after divide {}".format(num,div,num/div))
    print(num/div)
except ZeroDivisionError as e:
    logging.error("Zero division error got")
    print("Enter a valid diviser",e)
except Exception as E:
    logging.error("Error Got: {}".format(E))
    print("You got an error",E)
logging.info("-------------Code Execution Completed-------------")
logging.shutdown()
