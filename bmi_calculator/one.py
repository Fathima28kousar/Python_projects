def calculate_bmi(weight_kg,height_m):

    try:
        bmi = weight_kg/(height_m**2)
        
        if(bmi>0):
            if(bmi<=16):
                print("you are severely underweight")
            elif(bmi<=18.5):
                print("you are underweight")
            elif(bmi<=25):
                print("you are Healthy")
            elif(bmi<=30):
                print("you are overweight")
            else: print("you are severely overweight")
        return bmi
    
    except ZeroDivisionError:
        return "Height cannot be zero"

    except Exception as e:
        return f"An error occured: {e}"


def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight in Kilograms: "))
    height = float(input("Enter your height in Metres: "))

    bmi = calculate_bmi(weight,height)

    if isinstance (bmi,str):
        print(bmi)
    else:
        print(f"Your bmi is {bmi:.2f}")

if __name__ == '__main__':
    main()


