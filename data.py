import pygame

file_prefix = "assets/"

file_prefix_circle_rooms = file_prefix + "stations/circle/rooms/"

ships = [pygame.image.load(file_prefix + "ships/ship1.png")]
station_icon = pygame.image.load(file_prefix + "stations/icon.png")
stations = {
    "circle": {
        "base": pygame.image.load(file_prefix + "stations/circle/base.png"),
        "rooms": {
            "mission_centre": [pygame.image.load(file_prefix_circle_rooms + "mission_centre_1.png")],
            "ship_repair": [pygame.image.load(file_prefix_circle_rooms + "ship_repair.png")]
            }
        }
}

star_colors = [
    (255, 149, 41),
    (253, 204, 13),
    (255, 223, 0)
]

ui = {
    "pointer_down": pygame.image.load(file_prefix + "ui/pointer.png")
}

greek_alphabet = [
    "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", 
    "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", 
    "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", 
    "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"
]

english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

inventory = pygame.image.load(file_prefix + "inventory/crate.png")

star_names = ["Lynx", "Eridanus", "Eridanus", "Cassiopeia", "Scorpius", "Crux", "Cancer", "Leo", "Canis Major", "Andromeda", "Taurus", "Sagittarius", "Carina", "Lyra", "Serpens", "Lyra", "Sagittarius", "Aquarius", "Cygnus", "Corvus", "Ursa Major", "Taurus", "Taurus", "Cepheus", "Grus", "Draco", "Delphinus", "Cepheus", "Capricornus", "Pegasus", "Leo", "Perseus", "Corvus", "Gemini", "Ursa Major", "Cygnus", "Ursa Major", "Boötes", "Ursa Major", "Pegasus", "Crater", "Auriga", "Andromeda", "Leo", "Grus", "Sagittarius", "Orion", "Orion", "Scorpius", "Hydra", "Corona Borealis", "Andromeda", "Pisces", "Draco", "Pisces", "Draco", "Draco", "Lynx", "Vela", "Aquila", "Capricornus", "Aquila", "Draco", "Leo", "Canis Major", "Ursa Major", "Ursa Major", "Serpens", "Gemini", "Canis Major", "Crater", "Pegasus", "Vela", "aɲaˈɲuka", "Aquarius", "Eridanus", "Ursa Major", "Phoenix", "Vulpecula", "Scorpius", "Boötes", "Boötes", "Sagittarius", "Sagittarius", "Lepus", "Sagittarius", "Cancer", "Cancer", "Hydra", "Boötes", "Boötes", "Boötes", "Carina", "Taurus", "Canis Major", "Draco", "Perseus", "Taurus", "Triangulum Australe", "Carina", "Cetus", "Eridanus", "Cygnus", "Eridanus", "Puppis", "Ursa Minor", "Ophiuchus", "Cetus", "Indus", "Eridanus", "Eridanus", "Sagittarius", "Pisces", "Orion", "Perseus", "Orion", "Aries", "Sextans", "Pegasus", "Aquarius", "Aries", "Libra", "Mensa", "Andromeda", "Aquarius", "Carina", "Auriga", "Cassiopeia", "Gemini", "Cassiopeia", "Ophiuchus", "Chamaeleon", "Taurus", "Ara", "Ursa Major", "Taurus", "Eridanus", "Canes Venatici", "Lyra", "Aquila", "Leo", "Pisces", "Monoceros", "Sculptor", "Cancer", "Canes Venatici", "Hercules", "Eridanus", "Capricornus", "Fornax", "Tucana", "Cygnus", "Capricornus", "Leo", "Coma Berenices", "Puppis", "Leo", "Cetus", "Scorpius", "Fornax", "Centaurus", "Ursa Major", "Scorpius", "Ursa Major", "Draco", "Pisces", "Draco", "Taurus", "Virgo", "Columba", "Taurus", "Draco", "Tucana", "Pegasus", "Cepheus", "Draco", "Scorpius", "Cygnus", "Hydra", "Cetus", "Hydra", "Virgo", "Piscis Austrinus", "Leo", "Hercules", "Cassiopeia", "Pisces", "Draco", "Canis Major", "Scorpius", "Crux", "Cancer", "Virgo", "Cepheus", "Gemini", "Draco", "Corvus", "Crux", "Lynx", "Sextans", "Canis Minor", "Scorpius", "Virgo", "Draco", "Serpens", "Sagittarius", "Ophiuchus", "Centaurus", "Auriga", "Aries", "Auriga", "Orion", "Pegasus", "Virgo", "Taurus", "Pegasus", "Triangulum", "Crater", "Hercules", "Scorpius", "Leo Minor", "Crux", "Ara", "Fornax", "Ursa Major", "Hercules", "Grus", "Boötes", "Scorpius", "Gemini", "Cetus", "Cancer", "Vela", "Corona Borealis", "Virgo", "Apus", "Sagittarius", "Sagittarius", "Sagittarius", "Serpens", "Eridanus", "Virgo", "Equuleus", "Ursa Minor", "Eridanus", "Lynx", "Canes Venatici", "Hercules", "Columba", "Corvus", "Draco", "Cepheus", "Canes Venatici", "Scorpius", "Hydra", "Scorpius", "Aquila", "Virgo", "Ursa Major", "Aries", "Aquarius", "Auriga", "Monoceros", "Hercules", "Antlia", "Camelopardalis", "Auriga", "Ophiuchus", "Taurus", "Virgo", "Ophiuchus", "Pegasus", "Vela", "Aquarius", "Hercules", "Pegasus", "Centaurus", "Volans", "Ursa Major", "Gemini", "Ursa Major", "Orion", "Gemini", "Cancer", "Auriga", "Cetus", "Centaurus", "Perseus", "Ursa Major", "Boötes", "Corona Australis", "Taurus", "Aries", "Carina", "Crux", "Hydra", "Virgo", "Orion", "Cetus", "Andromeda", "Perseus", "Perseus", "Canis Major", "Perseus", "Ursa Major", "Corona Borealis", "Virgo", "Eridanus", "Pegasus", "Delphinus", "Triangulum", "Eridanus", "Cetus", "Canis Major", "Boötes", "Ursa Major", "Delphinus", "Perseus", "Cancer", "Dorado", "Puppis", "Capricornus", "Ursa Major", "Vela", "Cassiopeia", "Boötes", "Andromeda", "Phoenix", "Auriga", "Lepus", "Boötes", "Leo", "Puppis", "Sagittarius", "Corona Borealis", "Cassiopeia", "Centaurus", "Hercules", "Aquila", "Ophiuchus", "Scorpius", "Pisces", "Pavo", "Aquila", "Columba", "Ursa Major", "Ursa Minor", "Aquila", "Cancer", "Sagittarius", "Scorpius", "Hercules", "Taurus", "Tucana", "Ursa Minor", "Octans", "Sagittarius", "Gemini", "Virgo", "Leo Minor", "Taurus", "Canis Minor", "Gemini", "Centaurus", "Eridanus", "Eridanus", "Scorpius", "Leo", "Hercules", "Ophiuchus", "Draco", "Vela", "Leo", "Pisces", "Orion", "Centaurus", "Ophiuchus", "Delphinus", "Cassiopeia", "Sagittarius", "Ophiuchus", "Auriga", "Aquarius", "Pegasus", "Aquarius", "Aquarius", "Cygnus", "Leo", "Orion", "Pegasus", "Piscis Austrinus", "Sagitta", "Scorpius", "Hercules", "Eridanus", "Pegasus", "Cassiopeia", "Taurus", "Cassiopeia", "Boötes", "Sagitta", "Leo", "Scorpius", "Scorpius", "Lyra", "Aries", "Sagittarius", "Canis Major", "Aquarius", "Aquarius", "Pegasus", "Virgo", "Andromeda", "Lynx", "Delphinus", "Leo", "Vela", "Lyra", "Virgo", "Orion", "Lacerta", "Ursa Major", "Draco", "Ursa Major", "Pegasus", "Ursa Major", "Ursa Major", "Carina", "Aquila", "Cancer", "Taurus", "Cancer", "Gemini", "Sagittarius", "Auriga", "Orion", "Eridanus", "Draco", "Grus", "Taurus", "Draco", "Ophiuchus", "Puppis", "Andromeda", "Eridanus", "Centaurus", "Camelopardalis", "Pisces", "Canes Venatici", "Crux", "Reticulum", "Puppis", "Hydra", "Centaurus", "Serpens", "Canis Major", "Sagitta", "Sculptor", "Lyra", "Andromeda", "Virgo", "Gemini", "Vela", "Columba", "Canis Major", "Aquarius", "Phoenix", "Scorpius", "Lyra", "Boötes", "Ophiuchus", "Ophiuchus", "Ursa Minor", "Virgo", "Eridanus", "Virgo", "Aquarius"]
