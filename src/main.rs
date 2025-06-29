use std::process::Command;
use std::{thread, time::Duration};

fn check_firewall_status() -> bool {
    #[cfg(target_os = "macos")]
    {
        let output = Command::new("defaults")
            .arg("read")
            .arg("/Library/Preferences/com.apple.alf")
            .arg("globalstate")
            .output();

        if let Ok(output) = output {
            let result = String::from_utf8_lossy(&output.stdout);
            return result.trim() != "0";
        }
        false
    }

    #[cfg(not(target_os = "macos"))]
    {
        // Diğer platformlarda örnek kontrol (özelleştirilebilir)
        true
    }
}

fn main() {
    println!("🛡️ NeuroShield Firewall Kontrol Başlatılıyor...");
    
    loop {
        let aktif = check_firewall_status();
        if aktif {
            println!("✅ Firewall aktif.");
        } else {
            println!("⚠️ Firewall kapalı!");
        }

        thread::sleep(Duration::from_secs(10)); // 10 saniyede bir kontrol
    }
}


