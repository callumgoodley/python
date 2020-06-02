
# Create a paint requirement wizard that will calculate which of the following three products, would be the cheapest to buy, for the room you are painting.
# Work out which one wastes the least.
# Work out which is the best choice for any room(Cheapest).

# 1) CheapoMax(20Litre) £19.99
# This tin of paint will cover 10m2 per Litre
# 2) AverageJoes(15 Litre) £17.99
# This tin of paint will cover 11m2 per Litre
# 3) DuluxourousPaints(10 Litre) £25
# This tin of paint will cover 20m2 per Litre


def paint_wizard(room_size):
    Cheapomax = {
        "size": 20,
        "price": 19.99,
        "m2_per_litre": 10,
        "m2_per_tin": 200,
        "price_per_litre": 0.99
    }
    AverageJoes = {
        "size": 15,
        "price": 17.99,
        "m2_per_litre": 11,
        "m2_per_tin": 165,
        "price_per_litre": 1.19
    }
    DuluxourousPaints = {
        "size": 10,
        "price": 25,
        "m2_per_litre": 20,
        "m2_per_tin": 200,
        "price_per_litre": 2.50
    }

    waste_cheapo = Cheapomax["m2_per_tin"] % room_size
    waste_average_joes = AverageJoes["m2_per_tin"] % room_size
    waste_dulux = DuluxourousPaints["m2_per_tin"] % room_size

    price_cheapo = Cheapomax["price_per_litre"] * \
        (room_size / Cheapomax["m2_per_litre"])
    price_average_joes = AverageJoes["price_per_litre"] * \
        (room_size / AverageJoes["m2_per_litre"])
    price_dulux = float(DuluxourousPaints["price_per_litre"] *
                        (room_size / DuluxourousPaints["m2_per_litre"]))

    cheapest = ''
    least_waste = ''

    if waste_cheapo > waste_average_joes and waste_cheapo > waste_dulux:
        cheapest = "Using Cheapomax will leave you with the least waste"
    elif waste_average_joes > waste_cheapo and waste_average_joes > waste_dulux:
        cheapest = "Using AverageJoes will leave you with the least waste"
    elif waste_dulux > waste_cheapo and waste_dulux > waste_average_joes:
        cheapest = "Using DuluxourousPaints will leave you with the least waste"
    elif waste_dulux == waste_cheapo and waste_cheapo > waste_average_joes:
        cheapest = "DuluxourousPaints and Cheapomax will leave you with the equal amounts of waste and both less than AverageJoes"

    if price_cheapo < price_average_joes and price_cheapo < price_dulux:
        least_waste = "Cheapomax will be cheapest"
    elif price_average_joes < price_cheapo and price_average_joes < price_dulux:
        least_waste = "Average Joes will be cheapest"
    elif price_dulux < price_cheapo and price_dulux < price_average_joes:
        least_waste = "Dulux will be cheapest"
    return cheapest + " & " + least_waste
