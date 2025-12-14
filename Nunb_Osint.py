import requests
import os
import time
import re
from datetime import datetime, timedelta
import sys
import hashlib
import json
import uuid

try:
    from fpdf import FPDF
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("Install fpdf2 with: pip install fpdf2")

# COLORS 🎨
GREEN   = "\u001B[92m"
RED     = "\u001B[91m"
YELLOW  = "\u001B[93m"
CYAN    = "\u001B[96m"
MAGENTA = "\u001B[95m"
WHITE   = "\u001B[97m"
RESET   = "\u001B[0m"
GLITCH  = "\u001B[5m"

API_URL  = "https://numapi.anshapi.workers.dev/?num="
LICENSE_FILE = "spider_license.dat"

# DUAL KEY SYSTEM
TRIAL_KEY = "TRIAL-OSINT-2025-X9K7"
PERMANENT_KEY = "SUSOVAN0025"

# EMOJIS 🕷️🔥
SPIDER = "🕷️ "
FIRE = "🔥 "
TARGET = "🎯 "
PHONE = "📱 "
SUCCESS = "✅ "
ERROR = "❌ "
SCAN = "🔍 "
REPORT = "📄 "
LOCK = "🔐 "
KEY = "🔑 "
NO_DATA = "🚫 "
STAR = "⭐ "
BOLT = "⚡ "

HACKING_KEYWORDS = [
    "🔓 BREACHING DATABASE PERIMETER...",
    "💀 CRACKING ENCRYPTION LAYERS...",
    "⚡ BYPASSING FIREWALL DEFENSES...",
    "🧬 DNA TRACING INITIATED...",
    "🌐 TELECOM RECORDS HACKED...",
    "🕸️ SPIDER WEB DEPLOYED...",
    "🔍 DEEP SCANNING RECORDS...",
    "💻 SQL INJECTION SUCCESS...",
    "🗝️ KEYLOGGING ACTIVE...",
    "📡 SIGNAL INTERCEPTED...",
    "🎯 TARGET ACQUIRED...",
    "🔥 CONNECTION ESTABLISHED..."
]

# LICENSE FUNCTIONS
def get_device_id():
    """Generate unique device fingerprint"""
    try:
        hw_id = hashlib.md5(str(uuid.getnode()).encode()).hexdigest()[:16]
        ts = str(int(time.time()))
        device_id = hashlib.sha256((hw_id + ts).encode()).hexdigest()[:32]
        return device_id
    except:
        return "unknown-device-fallback"

def is_licensed():
    """Check if device is already activated"""
    try:
        if os.path.exists(LICENSE_FILE):
            with open(LICENSE_FILE, 'r') as f:
                data = json.load(f)
                return (data.get("status") == "activated" and 
                       data.get("device_id") == get_device_id())
    except:
        pass
    return False

def get_license_status():
    """Get current license info"""
    try:
        if os.path.exists(LICENSE_FILE):
            with open(LICENSE_FILE, 'r') as f:
                data = json.load(f)
                if data.get("device_id") == get_device_id():
                    # Check expiration for TRIAL
                    if data.get("key_type") == "TRIAL":
                        expires_at = datetime.fromisoformat(data.get("expires_at"))
                        if datetime.now() > expires_at:
                            return None  # Expired
                    return data
    except:
        pass
    return None

def activate_license(key):
    """Validate TRIAL (15min) or PERMANENT key"""
    device_id = get_device_id()
    
    license_type = None
    expires_at = None
    
    if key == TRIAL_KEY:
        license_type = "TRIAL"
        expires_at = (datetime.now() + timedelta(minutes=15)).isoformat()
    elif key == PERMANENT_KEY:
        license_type = "PERMANENT"
        expires_at = None
    else:
        return False
    
    license_data = {
        "status": "activated",
        "key_type": license_type,
        "device_id": device_id,
        "activated_at": datetime.now().isoformat(),
        "expires_at": expires_at
    }
    
    try:
        with open(LICENSE_FILE, 'w') as f:
            json.dump(license_data, f)
        return True
    except:
        return False

# HACKER INTERFACE FUNCTIONS
def hacker_frame(title="SPIDER OSINT v3.0"):
    clear()
    print(f"{GREEN}╔{'═' * 78}╗{RESET}")
    print(f"{GREEN}║{CYAN}{' ' * 76}{CYAN}║{RESET}")
    print(f"{GREEN}║{MAGENTA}{' ' * 34}{WHITE}{title.center(10)}{MAGENTA}{' ' * 34}║{RESET}")
    print(f"{GREEN}║{CYAN}{' ' * 76}{CYAN}║{RESET}")
    print(f"{GREEN}╠{'═' * 78}╣{RESET}")

def hacker_input_interface():
    hacker_frame("SPIDER OSINT v3.0")
    print(f"{GREEN}║{RESET}")
    print(f"{GREEN}║{RESET} {CYAN}[{GREEN}TARGET{RESET}] {MAGENTA}Phone (10-12 digits) or 'q'=quit:{RESET}", end="")
    for _ in range(3):
        print(f"{GLITCH}█{RESET}", end="", flush=True)
        time.sleep(0.3)
        print(" ", end="", flush=True)
        time.sleep(0.3)
    target = input(f"{RESET}").strip()
    return target

def hacker_status(phone):
    hacker_frame("CYBER RECON")
    print(f"{GREEN}║{RESET}")
    print(f"{GREEN}║{RESET} {TARGET} TARGET ACQUIRED: {CYAN}{phone}{RESET}")
    print(f"{GREEN}║{RESET} {SCAN} SCANNING DATABASES... {GREEN}████████░░ 80%{RESET}")
    print(f"{GREEN}║{RESET} {BOLT} EXPANDING NETWORK... {GREEN}██████████ 100%{RESET}")
    print(f"{GREEN}║{RESET}")
    print(f"{GREEN}╚{'═' * 78}╝{RESET}")
    time.sleep(1.5)

# TYPING FUNCTIONS
def type_text(text, color=GREEN, delay=0.02):
    for char in text:
        print(color + char + RESET, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(0.02)

def type_ultra_fast(text, color=GREEN, delay=0.008):
    for char in text:
        print(color + char + RESET, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(0.02)

def type_hacking_slow(text, color=GREEN, delay=0.035):
    for char in text:
        print(color + char + RESET, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(0.15)

def print_inline_ultra(text, color=GREEN, delay=0.005):
    for char in text:
        print(color + char + RESET, end='', flush=True)
        time.sleep(delay)

def clear():
    os.system("clear||cls")
    time.sleep(0.1)

# SCREENS
def welcome_screen():
    clear()
    type_ultra_fast("═" * 90, GREEN, 0.005)
    type_ultra_fast("🕷️" * 90, GREEN, 0.005)
    type_ultra_fast("🔥 WELCOME TO SPIDER OSINT V3.0 - CYBER INTELLIGENCE TOOL 🔥", GREEN, 0.008)
    type_ultra_fast("⚠️  GREAT POWER COMES WITH GREAT RESPONSIBILITY  ⚠️", YELLOW, 0.008)
    type_ultra_fast("🕷️  PREPARE FOR ADVANCED OSINT PHONE TRACKING MISSION  🕷️", GREEN, 0.008)
    type_ultra_fast("📱  DISCOVER HIDDEN CONNECTIONS AND UNIQUE NUMBERS  📱", GREEN, 0.008)
    type_ultra_fast("🔍  ENTERPRISE LEVEL CYBER INTELLIGENCE AT YOUR FINGERTIPS  🔍", GREEN, 0.008)
    type_ultra_fast("⚡  POWERED BY cutting-edge technology  ⚡", GREEN, 0.008)
    type_ultra_fast("═" * 90, GREEN, 0.005)
    time.sleep(0.5)
    
    type_ultra_fast("👨‍💻  MEET YOUR CREATOR AND MASTERMIND  👨‍💻", GREEN, 0.008)
    type_ultra_fast("NAME: SUSOVAN PATRA", GREEN, 0.008)
    type_ultra_fast("QUALIFICATION: B.TECH PASSOUT 2021", GREEN, 0.008)
    type_ultra_fast("AGE: 28 YEARS YOUNG", GREEN, 0.008)
    type_ultra_fast("LOCATION: WEST BENGAL, INDIA", GREEN, 0.008)
    type_ultra_fast("PROFESSION: GREY HAT HACKER", GREEN, 0.008)
    type_ultra_fast("SPECIALIZATION: PYTHON PROGRAMMING & CYBER SECURITY", GREEN, 0.008)
    
    type_ultra_fast("═" * 90, GREEN, 0.005)
    time.sleep(0.3)
    
    type_ultra_fast("🕷️  HACKING NAME: DEVIL CALL ME PAPA  🕷️", GREEN, 0.008)
    type_ultra_fast("💻  GITHUB: github.com/susovan266", GREEN, 0.008)
    type_ultra_fast("📱  TELEGRAM: @Devilcallmepapa", GREEN, 0.008)
    type_ultra_fast("📧  EMAIL: susovanpatra1997@gmail.com", GREEN, 0.008)
    type_ultra_fast("🔐  ENTERPRISE LICENSE REQUIRED FOR ACTIVATION", GREEN, 0.008)
    
    type_ultra_fast("═" * 90, GREEN, 0.005)
    type_ultra_fast("⚡ PRESS ENTER TO ACTIVATE SPIDER OSINT V3.0 ⚡", YELLOW, 0.02)
    input()
    clear()

def hacking_search_animation(target_phone):
    hacker_frame("HACKING SEQUENCE")
    type_ultra_fast(f"{TARGET}HACKING MODE ACTIVATED{STAR}", GREEN, 0.008)
    type_ultra_fast(f"{PHONE}TARGET: {target_phone}{TARGET}", GREEN, 0.008)
    type_ultra_fast("═" * 60, GREEN, 0.005)
    
    type_hacking_slow("🕷️ CYBER ATTACK SEQUENCE INITIATED 🕷️", GREEN, 0.04)
    type_hacking_slow("🚀 HACKING PHASES:", GREEN, 0.04)
    
    for i, keyword in enumerate(HACKING_KEYWORDS, 1):
        type_hacking_slow(f"  {i:2d}. {keyword}", GREEN, 0.035)
    
    type_hacking_slow(f"{BOLT} EXECUTING ALL PHASES SIMULTANEOUSLY... {BOLT}", GREEN, 0.04)
    type_hacking_slow(f"{SUCCESS}HACK COMPLETE! DATA EXTRACTED!{SUCCESS}", GREEN, 0.04)
    time.sleep(2)
    clear()

def print_banner():
    hacker_frame("SPIDER OSINT v3.0")
    type_ultra_fast("⚠️  GREAT POWER COMES WITH GREAT RESPONSIBILITY  ⚠️", YELLOW, 0.008)
    type_ultra_fast(f"{SPIDER}CREATED BY: SUSOVAN PATRA{SPIDER}", GREEN, 0.008)
    type_ultra_fast(f"{FIRE}HACKER: DEVIL CALL ME PAPA{FIRE}", GREEN, 0.008)
    type_ultra_fast(f"{PHONE}GITHUB: github.com/susovan266 | TG: @Devilcallmepapa{PHONE}", GREEN, 0.008)
    print(f"{GREEN}╚{'═' * 78}╝{RESET}")

def print_activation_menu():
    hacker_frame("🔐 LICENSE AUTH")
    type_ultra_fast(f"{LOCK}ENTERPRISE AUTHENTICATION REQUIRED{LOCK}", RED, 0.008)
    type_ultra_fast(f"{KEY}1️⃣  Trial (30min): Enter Your Trial Key", YELLOW, 0.008)
    type_ultra_fast(f"{KEY}2️⃣  Permanent: Enter Your Parmanent Key", GREEN, 0.008)
    type_ultra_fast(f"{KEY}3️⃣  Buy Enterprise 💰", CYAN, 0.008)
    type_ultra_fast(f"{ERROR}4️⃣  Exit 🚪", RED, 0.008)
    print_inline_ultra(f"{STAR}Choose (1-4): ", GREEN, 0.005)

def check_license():
    license_info = get_license_status()
    
    if license_info and license_info.get("status") == "activated":
        key_type = license_info.get("key_type", "UNKNOWN")
        if key_type == "PERMANENT":
            type_ultra_fast(f"{SUCCESS}🔓 PERMANENT LICENSE ACTIVE{SUCCESS}", GREEN, 0.008)
        else:
            type_ultra_fast(f"{SUCCESS}⏳ TRIAL ACTIVE (30min){SUCCESS}", YELLOW, 0.008)
        time.sleep(1.5)
        return True
    
    while True:
        print_activation_menu()
        try:
            choice = input().strip()
            
            if choice == "1":
                print_banner()
                type_ultra_fast(f"{YELLOW}🎁 TRIAL ACTIVATION (30min - 1 DEVICE){YELLOW}", YELLOW, 0.008)
                print_inline_ultra(f"{GREEN}Trial Key: {RESET}", GREEN, 0.005)
                key = input().strip()
                if activate_license(key):
                    type_ultra_fast(f"{SUCCESS}✅ TRIAL ACTIVATED! 30MIN ACCESS{SUCCESS}", GREEN, 0.008)
                    time.sleep(2)
                    return True
                else:
                    type_ultra_fast(f"{ERROR}❌ INVALID TRIAL KEY!{ERROR}", RED, 0.008)
                    
            elif choice == "2":
                print_banner()
                type_ultra_fast(f"{GREEN}🏆 PERMANENT ACTIVATION{GREEN}", GREEN, 0.008)
                print_inline_ultra(f"{GREEN}Permanent Key: {RESET}", GREEN, 0.005)
                key = input().strip()
                if activate_license(key):
                    type_ultra_fast(f"{SUCCESS}🎉 PERMANENT LICENSE UNLOCKED!{SUCCESS}", GREEN, 0.008)
                    type_ultra_fast(f"{STAR}Device LOCKED Forever{STAR}", YELLOW, 0.008)
                    time.sleep(2)
                    return True
                else:
                    type_ultra_fast(f"{ERROR}❌ INVALID PERMANENT KEY!{ERROR}", RED, 0.008)
                    
            elif choice == "3":
                show_contact_details()
            elif choice == "4":
                exit_animation()
            else:
                type_ultra_fast(f"{ERROR}Invalid option! 1-4{ERROR}", RED, 0.008)
                time.sleep(1)
        except KeyboardInterrupt:
            exit_animation()

# CORE FUNCTIONS
def print_animated_status(status_text, color=GREEN):
    type_ultra_fast(status_text, color, 0.008)

def parse_address(raw_addr):
    if not raw_addr:
        return "CLASSIFIED"
    parts = [p.strip() for p in raw_addr.split("!") if p.strip()]
    return ", ".join(parts)

def print_phone_results(phone, results, index):
    print(f"{PHONE}PHONE #{index}: {phone}")
    print("=" * 60)
    
    if not results:
        print(f"{NO_DATA}NO DATA{NO_DATA}")
        return
    
    for i, entry in enumerate(results, 1):
        print(f"{REPORT}RECORD {i}{REPORT}")
        print("-" * 40)
        
        primary = str(entry.get("mobile", "N/A"))
        name = str(entry.get("name", "N/A"))
        father = str(entry.get("father_name", "N/A"))
        addr = parse_address(entry.get("address", ""))
        alt = str(entry.get("alt_mobile", "N/A"))
        circle = str(entry.get("circle", "N/A"))
        idnum = str(entry.get("id_number", "CLASSIFIED"))
        email = str(entry.get("email", "N/A"))
        
        print(f"{PHONE}📱 Mobile: {primary}")
        print(f"👤 Name: {name}")
        print(f"👨 Father: {father}")
        print(f"📍 Address: {addr}")
        print(f"📱 Alt: {alt}")
        print(f"🌐 Network: {circle}")
        print(f"🆔 ID: {idnum}")
        print(f"📧 Email: {email}")
        print()

def osint_request(phone):
    try:
        url = API_URL + phone
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        return data if data.get("success") else None
    except:
        return None

def get_owner_name(phone):
    data = osint_request(phone)
    if not data or not data.get("success"):
        return "Unknown"
    results = data.get("result", [])
    if not isinstance(results, list):
        return "Unknown"
    for entry in results:
        if isinstance(entry, dict):
            name = entry.get("name", "").strip()
            if name and name != "N/A":
                clean_name = re.sub(r'[^ws-]', '', name).replace(" ", "_")[:30]
                return clean_name if clean_name else "Unknown"
    return "Unknown"

def safe_extract_phones(data):
    all_phones = set()
    if not data or not data.get("success"):
        return all_phones
    results = data.get("result", [])
    if not isinstance(results, list):
        return all_phones
    for entry in results:
        if isinstance(entry, dict):
            primary = str(entry.get("mobile", "")).strip()
            alt = str(entry.get("alt_mobile", "")).strip()
            if primary.isdigit() and len(primary) >= 10:
                all_phones.add(primary)
            if alt.isdigit() and len(alt) >= 10:
                all_phones.add(alt)
    return all_phones

def extract_unique_phones(initial_phone):
    all_phones = set()
    visited = set()
    frontier = [initial_phone]
    
    print_animated_status(f"{SCAN}FINDING ASSOCIATED NUMBERS...{SCAN}", GREEN)
    while frontier:
        phone = frontier.pop(0)
        if phone in visited:
            continue
        visited.add(phone)
        print_animated_status(f"[SCANNING] {phone}", GREEN)
        
        data = osint_request(phone)
        new_phones = safe_extract_phones(data)
        all_phones.update(new_phones)
        
        for new_phone in new_phones:
            if new_phone not in visited:
                frontier.append(new_phone)
        
        time.sleep(0.2)
    
    return sorted(list(all_phones))

def scan_unique_phone(phone):
    data = osint_request(phone)
    if not data or not data.get("success"):
        return []
    results = data.get("result", [])
    if not isinstance(results, list):
        return []
    unique_results = []
    seen_ids = set()
    for entry in results:
        if isinstance(entry, dict):
            entry_id = entry.get("id")
            if entry_id not in seen_ids:
                seen_ids.add(entry_id)
                entry["source_phone"] = phone
                unique_results.append(entry)
    return unique_results

def generate_pdf_report(initial_phone, unique_phones, timestamp, owner_name):
    if not PDF_AVAILABLE:
        print_animated_status(f"{REPORT}PDF generation not available. Install fpdf2", RED)
        return False
    
    safe_owner = owner_name[:30]
    filename = f"/storage/emulated/0/{safe_owner}_{timestamp}.pdf"
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "SPIDER OSINT V3.0", ln=1, align="C")
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, f"Generated: {timestamp}", ln=1, align="C")
    pdf.cell(0, 8, f"TARGET PHONE: {initial_phone}", ln=1, align="C")
    pdf.cell(0, 8, f"OWNER: {owner_name}", ln=1, align="C")
    pdf.cell(0, 8, f"TOTAL PHONES: {len(unique_phones)}", ln=1, align="C")
    pdf.ln(10)
    
    pdf.set_font("Helvetica", "", 12)
    for i, phone in enumerate(unique_phones, 1):
        results = scan_unique_phone(phone)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, f"PHONE #{i}: {phone}", ln=1)
        pdf.set_font("Helvetica", "", 10)
        if not results:
            pdf.cell(0, 8, "NO DATA", ln=1)
        else:
            for entry in results:
                pdf.cell(0, 6, f"Mobile: {entry.get('mobile', 'N/A')}", ln=1)
                pdf.cell(0, 6, f"Name: {entry.get('name', 'N/A')}", ln=1)
                pdf.cell(0, 6, f"Father: {entry.get('father_name', 'N/A')}", ln=1)
                pdf.cell(0, 6, f"Address: {parse_address(entry.get('address', ''))}", ln=1)
                pdf.cell(0, 6, f"Alt Mobile: {entry.get('alt_mobile', 'N/A')}", ln=1)
                pdf.cell(0, 6, f"Network: {entry.get('circle', 'N/A')}", ln=1)
                pdf.cell(0, 6, f"Email: {entry.get('email', 'N/A')}", ln=1)
                pdf.ln(2)
        pdf.ln(5)
    
    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "SUSOVAN PATRA - DEVIL CALL ME PAPA", ln=1, align="C")
    pdf.cell(0, 8, "GITHUB: github.com/susovan266", ln=1, align="C")
    pdf.cell(0, 8, "TELEGRAM: @Devilcallmepapa", ln=1, align="C")
    pdf.cell(0, 8, "EMAIL: susovanpatra1997@gmail.com", ln=1, align="C")
    
    pdf.output(filename)
    type_ultra_fast(f"{SUCCESS}Report saved: {filename}{SUCCESS}", GREEN, 0.008)
    return True

def display_unique_phones_report(initial_phone, unique_phones):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    owner_name = get_owner_name(initial_phone)
    
    hacker_frame("RESULTS REPORT")
    type_ultra_fast(f"{TARGET}TARGET: {initial_phone}", GREEN, 0.008)
    type_ultra_fast(f"👤 OWNER: {owner_name}", GREEN, 0.008)
    type_ultra_fast(f"{PHONE}UNIQUE PHONES: {len(unique_phones)}{PHONE}", GREEN, 0.008)
    
    for i, phone in enumerate(unique_phones, 1):
        print_animated_status(f"{SCAN}Scanning {i}/{len(unique_phones)}{SCAN}", GREEN)
        results = scan_unique_phone(phone)
        print_phone_results(phone, results, i)
        time.sleep(0.2)
    
    print("=" * 60)
    type_ultra_fast(f"{SUCCESS}SCAN COMPLETE!{SUCCESS}", GREEN, 0.008)
    
    print_inline_ultra(f"{REPORT}Save report as PDF? (y/n): ", GREEN, 0.005)
    save_choice = input().strip().lower()
    if save_choice == 'y':
        generate_pdf_report(initial_phone, unique_phones, timestamp, owner_name)
    
    input("Press Enter to continue...")

def show_contact_details():
    hacker_frame("CONTACT INFO")
    type_ultra_fast(f"{FIRE}💰 BUY ENTERPRISE LICENSE 💰{FIRE}", RED, 0.008)
    type_ultra_fast(f"{PHONE}📱 Telegram: @Devilcallmepapa", GREEN, 0.008)
    type_ultra_fast(f"{KEY}🔗 GitHub: github.com/susovan266", GREEN, 0.008)
    type_ultra_fast("📧 Email: susovanpatra1997@gmail.com", GREEN, 0.008)
    input("Press Enter to continue...")

def show_no_results_screen(phone):
    hacker_frame("NO RESULTS")
    type_ultra_fast(f"{NO_DATA}NO INFORMATION AVAILABLE{NO_DATA}", RED, 0.008)
    type_ultra_fast(f"{TARGET}TARGET: {phone}", GREEN, 0.008)
    type_ultra_fast(f"{NO_DATA}STATUS: NO DATA FOUND{NO_DATA}", RED, 0.008)
    input("Press Enter to search new number...")

def exit_animation():
    hacker_frame("DISCONNECTING")
    type_ultra_fast("🔥 THANK YOU FOR USING SPIDER OSINT V3.0 🔥", GREEN, 0.008)
    type_ultra_fast("🕷️ CYBER MISSION SUCCESSFULLY COMPLETED 🕷️", GREEN, 0.008)
    type_ultra_fast("⚡ STAY CYBER SAFE & HACK RESPONSIBLY ⚡", YELLOW, 0.008)
    time.sleep(2)
    clear()
    sys.exit(0)

def main():
    try:
        welcome_screen()
        
        while True:
            if check_license():
                break

        while True:
            target = hacker_input_interface()

            if target.lower() == "q":
                exit_animation()
                break

            if not target.isdigit() or len(target) < 10 or len(target) > 12:
                type_ultra_fast(f"{ERROR}❌ 10-12 DIGITS ONLY ❌{ERROR}", RED, 0.008)
                time.sleep(1)
                continue

            hacking_search_animation(target)
            hacker_status(target)
            
            print_animated_status(f"{SCAN}Initial analysis complete...{SCAN}")
            initial_data = osint_request(target)
            initial_phones = safe_extract_phones(initial_data)
            
            if not initial_phones:
                show_no_results_screen(target)
                continue

            print_animated_status(f"{SCAN}Expanding network connections...{SCAN}")
            unique_phones = extract_unique_phones(target)
            
            if not unique_phones:
                show_no_results_screen(target)
                continue
                
            display_unique_phones_report(target, unique_phones)
            
    except KeyboardInterrupt:
        exit_animation()

if __name__ == "__main__":
    main()