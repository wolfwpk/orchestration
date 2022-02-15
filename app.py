from flask import Flask, render_template, url_for, request, send_file, send_from_directory, Blueprint
from magenta.music import midi_io as mi
from magenta.music.protobuf import music_pb2
from google.protobuf.json_format import MessageToJson, Parse
import os


FILE_FOLDER = 'path/to/file_folder'
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/live', methods=['POST'])
def live_input():
    str1 = str(request.data, encoding="utf-8")
    global false, null, true
    false = null = true = ''
    data = eval(str1)
    seq = music_pb2.NoteSequence()
    # print(request.data)
    # seq.ParseFromString(request.data)
    # seq.ParseFromString(str1)

    seq.ticks_per_quarter = 220
    for note_message in data['notes']:
    #     print(note_message)
    # for index in [1,1,1,1]:
    #   note_message = data['notes'][0]
      note = seq.notes.add()
      note.program = note_message['program']
      note.start_time = note_message['startTime']
      note.end_time = note_message['endTime']
      note.pitch = note_message['pitch']
      note.velocity = note_message['velocity']
    tempo = seq.tempos.add()
    tempo.qpm = data['tempos'][0]['qpm']
    seq.total_time = data['totalTime']
    print(seq)
    mi.note_sequence_to_midi_file(seq,"midi/1.mid")
    os.system(' python venv/Lib/site-packages/magenta/models/gansynth/gansynth_generate.py --ckpt_dir=./ckpt/all_instruments --output_dir=./temp/wav --midi_file=./midi/1.mid')
    # return send_from_directory("temp/wav", "generated_clip.wav", as_attachment=True)
    return "1"

@app.route('/wav')
def get_wav():
    return send_from_directory("temp/wav", "generated_clip.wav", as_attachment=True)

def json_to_pb(jsonStringResponse):
  bidResponse = music_pb2.BidResponse()
  Parse(jsonStringResponse, bidResponse)
  pbStringResponse = bidResponse.SerializeToString()
  return pbStringResponse


app.run()
