
import pytest
from bs4 import BeautifulSoup

def parse_html():
    with open('submission/index.html', 'r', encoding='utf-8') as file:
        return BeautifulSoup(file.read(), 'html.parser')

def parse_css():
    with open('submission/style.css', 'r', encoding='utf-8') as file:
        return file.read()

def parse_js():
    with open('submission/script.js', 'r', encoding='utf-8') as file:
        return file.read()


# === BONUS TESTS ===

# --- HTML BONUS TESTS ---

def test_favicon_link():
    soup = parse_html()
    assert soup.find('link', rel='icon') is not None, "Favicon is not included in the <head>."

def test_section_ids_are_meaningful():
    soup = parse_html()
    sections = soup.find_all('section')
    for section in sections:
        sid = section.get('id')
        assert sid is not None and '-' in sid, "Section ID is missing or not meaningful (use kebab-case)."

def test_article_or_aside_used():
    soup = parse_html()
    assert soup.find('article') or soup.find('aside'), "No <article> or <aside> tags found."


# --- CSS BONUS TESTS ---

def test_dark_mode_support():
    css = parse_css()
    assert '@media (prefers-color-scheme: dark)' in css, "No dark mode support detected."

def test_custom_font_imported():
    css = parse_css()
    assert '@import url(' in css or 'fonts.googleapis.com' in css, "Custom font not imported."

def test_css_animation():
    css = parse_css()
    assert '@keyframes' in css or 'animation:' in css, "No CSS animation detected."

def test_responsive_typography():
    css = parse_css()
    assert 'clamp(' in css or 'vw' in css or 'rem' in css, "Responsive typography not found (use clamp, rem, vw, etc.)."


# --- JS BONUS TESTS ---

def test_js_uses_template_literals():
    js = parse_js()
    assert '`' in js and '${' in js, "No usage of template literals found in JavaScript."

def test_local_or_session_storage():
    js = parse_js()
    assert 'localStorage.' in js or 'sessionStorage.' in js, "No use of localStorage or sessionStorage."

def test_interaction_feedback():
    js = parse_js()
    keywords = ['classList.add', 'innerHTML', 'textContent', 'disabled', 'toggle']
    assert any(k in js for k in keywords), "No dynamic feedback behavior found on user interaction."

def test_form_validation_logic():
    js = parse_js()
    assert 'checkValidity' in js or 'regex' in js or '.test(' in js, "No form validation logic found."

def test_modular_code_structure():
    js = parse_js()
    assert 'export ' in js or 'import ' in js, "JavaScript modular code structure (ES Modules) not detected."

