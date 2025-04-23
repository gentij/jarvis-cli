import typer
from modules.speech_to_text import transcribe_audio
from modules.llm_query import get_command_from_llm

def listen():
    """
    Voice-commanded assistant that listens and suggests a shell command.
    """
    typer.echo("🎙️ Listening... Speak your command.")
    audio_file = "output.wav"

    # Transcribe
    text = transcribe_audio(audio_file)
    typer.echo(f"📝 Transcribed: {text}")

    # Get LLM suggestion
    suggested_cmd = get_command_from_llm(text)
    typer.echo(f"🤖 Suggested Command: {suggested_cmd}")

    # Confirm to run
    confirm = input("⚠️ Run this command? [y/N] ")
    if confirm.lower() == "y":
        import subprocess
        subprocess.run(suggested_cmd, shell=True)

if __name__ == "__main__":
    typer.run(listen)
