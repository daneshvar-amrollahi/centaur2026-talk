tell application "Keynote"
	set doc to document "talk"
	set out to ""
	repeat with s in slides of doc
		set t to ""
		if title showing of s then set t to (object text of default title item of s as text)
		if t is "" then
			try
				set t to (object text of default body item of s as text)
			end try
		end if
		set out to out & "## Slide " & (slide number of s) & ": " & t & linefeed & linefeed
		set out to out & (presenter notes of s as text) & linefeed & linefeed
	end repeat
end tell
return out
