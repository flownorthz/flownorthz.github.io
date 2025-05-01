function runLoop(i = 0, max = 1000) {
    if (i >= max) return;

    // โค้ดหลักเริ่มที่นี่

    const ReactKey = (elem, prefix) => {
        if (elem == null || elem == undefined) {
            return;
        }
        let key = Object.keys(elem).find(key => key.startsWith(prefix));
        return elem[key];
    };

    const ReactEvents = (elem) => {
        return ReactKey(elem, "__reactEventHandlers$");
    };

    //
    
    const continueButton = Array.from(document.querySelectorAll('button'))
        .find(button => button.textContent.trim() === 'Continue');

    //
    const delay = Math.floor(Math.random() * 1000) + 1000;

    setTimeout(() => {
        console.log(`🔁 เริ่มรอบที่ ${i + 1} (delay: ${delay}ms)`);
    //
    
        if (continueButton) {
            continueButton.click();
        } else {
            console.log('ไม่พบปุ่ม Continue');
        }

        const elementsWithPass = [...document.querySelectorAll('[data-qa-pass]')];

        const sorted = elementsWithPass.sort((a, b) => {
            const aVal = a.getAttribute('data-qa-pass');
            const bVal = b.getAttribute('data-qa-pass');
            const aNum = parseInt(aVal);
            const bNum = parseInt(bVal);
            if (!isNaN(aNum) && !isNaN(bNum)) {
                return aNum - bNum;
            }
            return 0;
        });

        sorted.forEach((el, idx) => {
            el.style.border = '2px solid orange';
            el.style.padding = '4px';
            console.log(`📍 ลำดับ ${idx + 1} | data-qa-pass: ${el.getAttribute('data-qa-pass')} | ข้อความ: "${el.innerText.trim()}"`);

            el.click();

            const word = el.getAttribute('data-qa-pass');
            if (word && isNaN(Number(word)) && word !== "true") {
                const input = el.closest('form')?.querySelector('input') || document.querySelector('input');
                if (input) {
                    const onChangeEvent = ReactEvents(input);
                    if (onChangeEvent) {
                        onChangeEvent.onChange({ target: { value: word } });
                        console.log(`✍️ ใส่ "${word}" ลงใน input แล้ว`);

                        const checkButton = document.querySelector("[data-testid='check_button']");
                        if (checkButton) {
                            checkButton.click();
                        } else {
                            console.log("⚠️ ไม่พบปุ่ม check_button");
                        }
                    }
                } else {
                    console.log("⚠️ ไม่เจอ input ให้กรอก");
                }
            }
        });

        // รันรอบถัดไป
        runLoop(i + 1, max);
    }, delay);
}

// เริ่มลูป
runLoop();
