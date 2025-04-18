# 🧠 Post-Incident Notes – Cron Job Persistence

## 🔍 Incident Summary
A persistent cron job was discovered in the user's crontab, scheduled to execute every minute. It wrote logs to a hidden file and could have been replaced with any payload.

## 🔧 Actions Taken
- Crontab entry removed
- Script `/tmp/malicious.sh` deleted
- Output log `/tmp/.cron.log` deleted
- Cron service restarted to ensure changes applied

## 🛡️ Recommendations
- Enable monitoring of `/var/spool/cron/crontabs` and `/etc/cron*`
- Set up alerts using `auditd` or `inotify` for unauthorized cron changes
- Educate users about dangers of executing scripts from `/tmp`
- Implement least privilege: restrict who can schedule cron jobs

## ✅ Next Steps
- Run full malware scan (e.g., ClamAV or rkhunter)
- Check for additional persistence (rc.local, systemd timers, etc.)
- Archive evidence (logs, script copy, screenshot set)
