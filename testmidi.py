from magenta.music import midi_io as mi
from magenta.music.protobuf import music_pb2
import os



os.system('python venv/Lib/site-packages/magenta/models/gansynth/gansynth_generate.py --ckpt_dir=./ckpt/all_instruments --output_dir=./temp/wav --midi_file=./1.mid')


# seq = music_pb2.NoteSequence()
# seq = mi.midi_file_to_sequence_proto("1.mid")
# str1 = seq.SerializeToString()
# print(type(str1))
# str2 = str1.decode('GB2312')
# print(str2)
# seq2 = music_pb2.NoteSequence()
# seq2.ParseFromString(str1)
# print(str1)
# print(seq2)



# data = {'ticks_per_quarter': 220,
#         "time_signatures": {
#             "numerator": 4,
#             "denominator": 4,
#         },
#         "tempos": {
#             "qpm": 120.0
#         },
#         "notes": [{"pitch": 53, "velocity": 40, "program": 26, "startTime": 0.54, "endTime": 0.79},
#                   {"pitch": 50, "velocity": 40, "program": 26, "startTime": 0.9400000000000001, "endTime": 1.19}],
#         "totalTime": 1.19
#         }
# json = json.dumps(data)
# print(json.ticks_per_quarter)
# mi.note_sequence_to_midi_file(json, "./midi/1.mid")
