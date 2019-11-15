import argparse
import bach.geometry
import bach.entities
import bach.behavior


def command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="The file containing the position of entities", type=str)
    parser.add_argument("--ghost_threshold",
                        help="Number of frames without a new detection before the entity becomes a ghost",
                        type=int, default=25)
    # Debug
    parser.add_argument("--debug", help="Debug mode", action="store_true")
    return parser.parse_args()


def analysis(arguments, input_file):
    frame_counter = 0
    entities = dict()
    encounters = list()
    for line in input_file:
        if line[0] == "#":
            continue
        items = line.split(sep=" ")
        frame_counter = int(items[0])
        new_point = bach.geometry.Point(float(items[2]), float(items[3]))
        if items[1] in entities:
            entities[items[1]].update_position(new_point)
            entities[items[1]].update_size(items[4], items[5])
        else:
            entity = bach.entities.Entity(marker=int(items[1]),
                                          width=float(items[4]),
                                          height=float(items[5]),
                                          seen=frame_counter)
            entity.position = new_point
            entity.box = bach.geometry.Rectangle(new_point, float(items[4]), float(items[5]))
            entities[items[1]] = entity
    # Behavior detection
    bach.behavior.encounter(frame_counter, entities.values(), encounters)
    if arguments.debug:
        print("# Encounters: {}".format(len(encounters)))
    for encounter in encounters:
        if arguments.debug:
            print("\t# Encounter: (\"{} {}\", \"{} {}\"), duration: {}".format(encounter.participants[0].label,
                                                                               encounter.participants[0].marker,
                                                                               encounter.participants[1].label,
                                                                               encounter.participants[1].marker,
                                                                               encounter.last - encounter.begin))
        if encounter.last < frame_counter - arguments.ghost_threshold:
            encounters.remove(encounter)
    if arguments.debug:
        print()


def __main__():
    arguments = command_line()
    input_file = open(arguments.file)
    if not input_file:
        print("Impossible to open input")
        exit(-1)
    analysis(arguments, input_file)
    input_file.close()
    return 0


__main__()
