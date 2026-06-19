---
name: Forensic Audio Transcriber
version: "1.0.0"
depends_on: [mcp-mastery, cryptographic-integrity-monitor, token-economy]
council: EARTH
description: Multi-engine audio forensic analysis and transcription system. Ingests audio/video files, performs speaker diarization, multi-language transcription, acoustic environment analysis, tampering detection, and voice biometric profiling. Produces chain-of-custody auditable transcripts with confidence-tagged segments.
---

# Forensic Audio Transcriber

## Directives

1. **Multi-Engine Transcription Pipeline:**
   - Primary engines: Whisper (local), Deepgram (cloud), AssemblyAI (cloud) — run in parallel for cross-validation.
   - Language auto-detection with manual override for mixed-language recordings.
   - Speaker diarization: identify and label distinct speakers, track speaker turns.
   - Confidence scoring per transcribed segment; flag low-confidence (<80%) segments for human review.
   - Timestamp alignment at word level where engine supports it.

2. **Acoustic Forensics Layer:**
   - Background noise classification: identify environment type (office, street, vehicle, indoor, outdoor).
   - Audio tampering detection: detect splices, overdubs, frequency artifacts, compression fingerprints.
   - Recording device fingerprinting: identify device class from acoustic signature (microphone type, codec artifacts).
   - Spectrogram analysis for non-verbal audio events (gunshots, impacts, alarms, vehicle sounds).
   - Silence/pause pattern analysis for behavioral indicators.

3. **Voice Biometric Profiling:**
   - Speaker age-range estimation from vocal characteristics.
   - Gender identification from fundamental frequency and formant analysis.
   - Emotion/tone detection per speaker segment: stress markers, deception indicators (vocal tension, pitch variance).
   - Accent/dialect classification with regional confidence scoring.
   - Cross-recording speaker matching: identify same speaker across different audio files.

4. **Chain of Custody & Integrity:**
   - Every source audio file hashed (SHA-256) on ingestion; hash recorded in output manifest.
   - All processing steps logged with timestamps and engine versions.
   - Transcript immutable once finalized — edits create new version with diff tracking.
   - cryptographic-integrity-monitor: hash chain from source audio through all derived artifacts.

5. **Output Artifacts:**
   - Full transcript with speaker labels, timestamps, confidence scores.
   - Speaker diarization report: speaker count, turn distribution, overlap analysis.
   - Acoustic environment report: noise profile, tampering assessment, device fingerprint.
   - Voice biometric dossier per speaker.
   - Chain-of-custody manifest with all hashes.
   - Low-confidence segment report flagged for human review.

6. **Governance:**
   - security-guard: audio files treated as potentially sensitive; never stored beyond session without user approval.
   - immutable-core-directives: transcription must be faithful to source; no editorializing or omission.
   - token-economy: large audio files chunked; only process segments relevant to query.
   - Compliance: consent verification required for recordings involving non-public individuals.

7. **Integration Map:**
   - **Upstream**: browser-use-agent (audio source acquisition), web-devourer (podcast/stream ingestion), mcp-business-integrations (media storage).
   - **Downstream**: omni-profiler-swarm (voice biometrics feed), legal-expert-swarm (deposition/hearing transcripts), clinical-diagnostician (speech pattern analysis), magic-deduction-swarm (disputed content analysis).
   - **Governing**: security-guard, immutable-core-directives, cryptographic-integrity-monitor.
   - **Council**: EARTH (Structure & Crystal domain).
