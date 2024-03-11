# Step 1: make a dynamic list of workers
workers = []

for i in range(1, 486):
    worker = {
        "id": i,
        "name": f"Worker {i}",
        "gender": "female" if i % 2 == 0 else "male",
        "salary": 5000 + i * 25
    }
    workers.append(worker)

# Step 2: produce pay slip for each worker and apply conditions
for worker in workers:
    try:
        salary = worker["salary"]
        if 10000 < salary < 20000:
            worker["level"] = "A1"
        elif 7500 < salary < 30000 and worker["gender"] == "female":
            worker["level"] = "A5-F"
        else:
            worker["level"] = "Regular"

        print(f"Payment Slip for {worker['name']} - Level: {worker['level']}, Salary: ${salary}")
    except KeyError as e:
        print(f"Missing key: {e} for worker {worker['id']}")
    except Exception as e:
        print(f"Error occurred for worker {worker['id']}: {e}")