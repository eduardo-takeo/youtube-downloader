# FIXME: 
# - [ ] Gerar arquivo de log para cada vídeo baixado
# - [ ] Melhorar mensagens de erro

import os
import yt_dlp


def download_audio(video_url, output_folder, error_file):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'nocheckcertificate': True,
            'ignoreerrors': True,
            'no_warnings': True,
            'quiet': False,
            'extract_flat': False,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            }
        }
        # Verifica se a URL é válida antes de tentar o download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.extract_info(video_url, download=False)
                # Se chegou aqui, a URL é válida, então faz o download
                ydl.download([video_url])
                print(f"Download concluído: {video_url}")
            except Exception as e:
                # URL inválida ou erro no download
                with open(error_file, 'a', encoding='utf-8') as f:
                    f.write(f"{video_url} - Erro: {str(e)}\n")
                print(f"Erro ao processar o vídeo {video_url}: {e}")
                
    except Exception as e:
        with open(error_file, 'a', encoding='utf-8') as f:
            f.write(f"{video_url} - Erro: {str(e)}\n")
        print(f"Erro ao processar o vídeo {video_url}: {e}")


def main():
    # Arquivo contendo os links
    input_file = "links.txt"
    # Pasta de saída
    output_folder = "downloads"
    error_file = "errors.txt"
    os.makedirs(output_folder, exist_ok=True)
    
    # Limpa o arquivo de erros se ele existir
    if os.path.exists(error_file):
        os.remove(error_file)

    # Verifica se o arquivo existe
    if not os.path.exists(input_file):
        print(
            f"Arquivo {input_file} não encontrado. Certifique-se de que ele existe.")
        return

    # Lê os links do arquivo
    with open(input_file, "r") as file:
        video_urls = [line.strip() for line in file if line.strip()]

    if not video_urls:
        print(
            f"O arquivo {input_file} está vazio. Adicione links do YouTube (um por linha).")
        return

    # Processar cada URL
    for url in video_urls:
        download_audio(url, output_folder, error_file)

    if os.path.exists(error_file) and os.path.getsize(error_file) > 0:
        print(f"\nAlguns vídeos não puderam ser baixados. Verifique {error_file} para mais detalhes.")
    
    print("\nTodos os downloads concluídos!")


if __name__ == "__main__":
    main()
