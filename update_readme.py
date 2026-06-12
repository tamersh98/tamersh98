import os
import requests

def get_dynamic_content():
    """Fetch a daily programming quote or any API data."""
    try:
        response = requests.get("https://api.quotable.io/random?tags=technology,famous-quotes")
        if response.status_code == 200:
            data = response.json()
            return f"\n> \"{data['content']}\" — *{data['author']}*\n"
    except Exception as e:
        print(f"Error fetching data: {e}")
    
    # Fallback content if the API fails
    return "\n> \"Code is like humor. When you have to explain it, it’s bad.\" — *Cory House*\n"

def update_readme():
    # 1. Fetch the new content
    new_content = get_dynamic_content()
    
    # 2. Read the existing README
    with open("README.md", "r", encoding="utf-8") as file:
        readme_text = file.read()

    # 3. Define the anchors
    start_anchor = ""
    end_anchor = ""

    # 4. Find the positions of the anchors
    start_idx = readme_text.find(start_anchor)
    end_idx = readme_text.find(end_anchor)

    if start_idx == -1 or end_idx == -1:
        print("Anchors not found in README.md!")
        return

    # 5. Slice the text and insert the new content between the anchors
    updated_text = (
        readme_text[:start_idx + len(start_anchor)]
        + new_content
        + readme_text[end_idx:]
    )

    # 6. Write the changes back to README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_text)
        
    print("README.md updated successfully!")

if __name__ == "__main__":
    update_readme()
