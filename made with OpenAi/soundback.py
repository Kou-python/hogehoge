import pyaudio
import wave

# 録音パラメータ
FORMAT = pyaudio.paInt16 # 音声のフォーマット
CHANNELS = 1             # モノラル
RATE = 44100             # サンプルレート
CHUNK = 2**11            # データ点数
RECORD_SECONDS = 5       # 録音する時間の長さ
WAVE_FILE = "sample.wav" # 音声を保存するファイル名

# pyaudioのインスタンスを生成
p = pyaudio.PyAudio()

# 録音用のストリームを開く
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("録音開始...")

# 録音データを格納するリスト
frames = []

# 指定した時間だけ録音
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("録音終了...")

# ストリームを閉じる
stream.stop_stream()
stream.close()
p.terminate()

# 録音データをファイルに保存
wf = wave.open(WAVE_FILE, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
