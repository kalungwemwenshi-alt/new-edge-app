/**
 * EdgeGrid Interactive Position & Risk Terminal
 */

document.addEventListener('DOMContentLoaded', () => {
    const calcBtn = document.getElementById('calculateBtn');
    const pairSelect = document.getElementById('currencyPair');
    const balanceInput = document.getElementById('accountBalance');
    const riskInput = document.getElementById('riskPercentage');
    const stopLossInput = document.getElementById('stopLoss');
    const errorMsg = document.getElementById('errorMsg');
    const riskBadge = document.getElementById('riskPercentBadge');
    const safetyBadge = document.getElementById('riskSafetyBadge');

    function calculate() {
        if (!pairSelect || !balanceInput || !riskInput || !stopLossInput) return;

        const pairPipValue = parseFloat(pairSelect.value);
        const balance = parseFloat(balanceInput.value);
        const riskPct = parseFloat(riskInput.value);
        const stopLoss = parseFloat(stopLossInput.value);

        if (riskBadge) {
            riskBadge.textContent = `${riskPct ? riskPct.toFixed(1) : 0}%`;
        }

        if (isNaN(balance) || isNaN(riskPct) || isNaN(stopLoss) || balance <= 0 || riskPct <= 0 || stopLoss <= 0) {
            if (errorMsg) errorMsg.style.display = 'block';
            resetResults();
            return;
        }

        if (errorMsg) errorMsg.style.display = 'none';

        // USD Risk Amount
        const riskAmount = balance * (riskPct / 100);
        
        // Lots Calculation: Lots = Risk Amount / (Pip Value * StopLoss)
        const standardLots = riskAmount / (pairPipValue * stopLoss);
        const miniLots = standardLots * 10;
        const microLots = standardLots * 100;

        // Approx ZMW conversion (approx 27 ZMW per 1 USD)
        const zmwRisk = riskAmount * 27;

        // Display results
        const moneyRiskEl = document.getElementById('moneyRisk');
        const standardLotsEl = document.getElementById('standardLots');
        const miniLotsEl = document.getElementById('miniLots');
        const microLotsEl = document.getElementById('microLots');
        const kwachaRiskEl = document.getElementById('kwachaRisk');

        if (moneyRiskEl) moneyRiskEl.textContent = `$${riskAmount.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        if (standardLotsEl) standardLotsEl.textContent = standardLots < 0.01 ? standardLots.toFixed(3) : standardLots.toFixed(2);
        if (miniLotsEl) miniLotsEl.textContent = miniLots.toFixed(2);
        if (microLotsEl) microLotsEl.textContent = microLots.toFixed(2);
        if (kwachaRiskEl) kwachaRiskEl.textContent = `~K${zmwRisk.toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: 0 })} ZMW`;

        // Safety Status Badge
        if (safetyBadge) {
            if (riskPct <= 1.5) {
                safetyBadge.textContent = 'PRO RECOMMENDED';
                safetyBadge.style.background = 'rgba(0, 186, 102, 0.15)';
                safetyBadge.style.color = '#00BA66';
            } else if (riskPct <= 3.0) {
                safetyBadge.textContent = 'MODERATE RISK';
                safetyBadge.style.background = 'rgba(245, 158, 11, 0.15)';
                safetyBadge.style.color = '#F59E0B';
            } else {
                safetyBadge.textContent = 'HIGH CAPITAL HAZARD';
                safetyBadge.style.background = 'rgba(239, 68, 68, 0.15)';
                safetyBadge.style.color = '#EF4444';
            }
        }
    }

    function resetResults() {
        const fields = ['moneyRisk', 'standardLots', 'miniLots', 'microLots', 'kwachaRisk'];
        fields.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.textContent = '0.00';
        });
    }

    if (calcBtn) {
        calcBtn.addEventListener('click', (e) => {
            e.preventDefault();
            calculate();
        });
    }

    // Auto calculate on input change for real-time responsiveness
    [pairSelect, balanceInput, riskInput, stopLossInput].forEach(el => {
        if (el) {
            el.addEventListener('input', calculate);
            el.addEventListener('change', calculate);
        }
    });

    window.triggerCalculation = calculate;

    // Run initial calculation
    calculate();
});
