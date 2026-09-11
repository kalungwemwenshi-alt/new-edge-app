# modules_part3.py
# Comprehensive content for Module 6 & Module 7

MODULE_6 = """            <!-- MODULE 6 -->
            <div class="module-content-pane" id="module-6">
                <div class="module-hero">
                    <span class="module-number">Macro Catalysts</span>
                    <h1>Module 6: Macro Fundamentals & High-Impact Catalyst Trading</h1>
                    <p>Deciphering central bank policy, interest rate differentials, inflation metrics, sentiment regimes, and news trading defense.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 75%;"></div>
                    </div>
                </div>

                <!-- 1. THE REAL PURPOSE OF FUNDAMENTALS -->
                <div class="content-section">
                    <h3><i class='bx bx-globe'></i> 1. The Real Purpose of Fundamentals for Technical Traders</h3>
                    <p>Retail traders mistakenly believe that economic news creates random, unpredictable chaotic moves. To institutional desks, <strong>macro catalysts are the volatility injection mechanism</strong> used to deliver price swiftly to technical higher-timeframe order blocks and liquidity pools. Fundamentals provide the <em>fuel</em>; technical market structure provides the <em>roadmap</em>.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid var(--vip-gold);">
                            <h4 style="color: var(--vip-gold); margin-bottom: 8px;">Macro Fundamentals (The Compass)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Dictates the multi-month macroeconomic trend through interest rate differentials, central bank balance sheets, and sovereign bond yields. Answers <strong>"Which currency has institutional capital accumulation?"</strong></p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">SMC Technical Order Flow (The Timing)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Dictates the exact entry, stop loss, and take profit boundaries. Pinpoints the Order Blocks, Fair Value Gaps, and Session Kill Zones. Answers <strong>"When and at what price level do we enter?"</strong></p>
                        </div>
                    </div>
                </div>

                <!-- 2. THE BIG 3 HIGH-IMPACT CATALYSTS -->
                <div class="content-section">
                    <h3><i class='bx bx-bell'></i> 2. The Big 3 High-Impact Market Drivers</h3>
                    <p>Over 80% of major market repricing events are driven by three recurring macroeconomic releases:</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Catalyst</th>
                                    <th>Release Schedule</th>
                                    <th>Average Pip Impact</th>
                                    <th>Institutional Metric Analyzed</th>
                                    <th>Directional Rule</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>NFP (Non-Farm Payrolls)</strong></td>
                                    <td>1st Friday of month (13:30 GMT)</td>
                                    <td>80 - 150+ Pips</td>
                                    <td>Job Creation, Unemployment Rate, Wage Growth</td>
                                    <td>Higher jobs + higher wages = Bullish USD</td>
                                </tr>
                                <tr>
                                    <td><strong>CPI (Consumer Price Index)</strong></td>
                                    <td>Mid-Month (13:30 GMT)</td>
                                    <td>100 - 200+ Pips</td>
                                    <td>Core Inflation vs Central Bank 2.0% Target</td>
                                    <td>Hotter inflation = Rate hikes = Bullish Currency</td>
                                </tr>
                                <tr>
                                    <td><strong>FOMC / Central Bank Rates</strong></td>
                                    <td>Every 6 Weeks (18:00 GMT)</td>
                                    <td>120 - 250+ Pips</td>
                                    <td>Benchmark Rate Decision & Forward Guidance</td>
                                    <td>Hawkish surprise = Violent expansion in currency</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 3. CENTRAL BANK RATE CYCLE SCHEMATIC -->
                <div class="content-section">
                    <h3><i class='bx bx-trending-up'></i> 3. Central Bank Interest Rate Differentials & Macro Cycles</h3>
                    <p>Capital always flows towards where it yields the highest risk-adjusted return. When Central Bank A is raising interest rates (Hawkish) while Central Bank B is cutting rates (Dovish), the interest rate differential creates a powerful multi-month institutional macro trend.</p>

                    <!-- SVG 5: Macro Rate Cycle Schematic -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- Cycle Sine Wave -->
                                <path d="M 50 150 Q 200 20 400 150 T 750 150" fill="none" stroke="#555" stroke-width="2" stroke-dasharray="4,4" />

                                <!-- Hawkish Tightening Phase -->
                                <path d="M 50 150 Q 200 20 400 150" fill="none" stroke="#00ff88" stroke-width="3" />
                                <rect x="130" y="45" width="200" height="50" fill="rgba(0, 255, 136, 0.12)" stroke="#00ff88" stroke-width="1.5" rx="4" />
                                <text x="230" y="68" fill="#00ff88" font-size="12" font-weight="700" text-anchor="middle">HAWKISH CYCLE (RATE HIKES)</text>
                                <text x="230" y="84" fill="#ddd" font-size="9" text-anchor="middle">Fighting Inflation -> Currency Appreciates</text>

                                <!-- Dovish Easing Phase -->
                                <path d="M 400 150 Q 600 280 750 150" fill="none" stroke="#ff4444" stroke-width="3" />
                                <rect x="470" y="205" width="200" height="50" fill="rgba(255, 68, 68, 0.12)" stroke="#ff4444" stroke-width="1.5" rx="4" />
                                <text x="570" y="228" fill="#ff4444" font-size="12" font-weight="700" text-anchor="middle">DOVISH CYCLE (RATE CUTS)</text>
                                <text x="570" y="244" fill="#ddd" font-size="9" text-anchor="middle">Stimulating Growth -> Currency Depreciates</text>

                                <!-- Midpoint Equilibrium Line -->
                                <line x1="50" y1="150" x2="750" y2="150" stroke="var(--vip-gold)" stroke-width="1" stroke-dasharray="2,2" />
                                <text x="70" y="142" fill="var(--vip-gold)" font-size="10">Neutral Benchmark (2.0%)</text>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The Monetary Policy Cycle: Trade in alignment with central bank divergence. Buy currencies with rising rate expectations against currencies cutting rates.</p>
                    </div>
                </div>

                <!-- 4. RISK-ON VS RISK-OFF SENTIMENT -->
                <div class="content-section">
                    <h3><i class='bx bx-shuffle'></i> 4. Risk-On vs Risk-Off Sentiment Matrix</h3>
                    <p>Global markets operate under two primary psychological regimes. Understanding market sentiment tells you where institutional capital is rotating.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">Risk-On Regime (Greed / Growth)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Global equities rally. Investors seek high yield. Capital flows into <strong>AUD, NZD, GBP, and Emerging Markets</strong>. Safe havens (USD, CHF, JPY) are sold off.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">Risk-Off Regime (Fear / Panic)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Geopolitical tension or economic recession. Capital seeks capital preservation. Heavy flows into <strong>Gold (XAU), US Dollar (USD), Swiss Franc (CHF), and Japanese Yen (JPY)</strong>.</p>
                        </div>
                    </div>
                </div>

                <!-- 5. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 5. VIP Interactive Tool: Macro Catalyst & Economic Bias Evaluator</h3>
                    <p>Input recent economic data deltas and interest rate expectations to determine the institutional directional bias for any major currency pair.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-globe'></i> Macro Sentiment Evaluator</h4>
                            <span class="badge-institutional">MODULE 6 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-trending-up'></i> Interest Rate Differential</label>
                                <select id="m6RateDiff">
                                    <option value="base_higher">Base Currency Rates Higher / Hiking (+30 Pts Base)</option>
                                    <option value="quote_higher">Quote Currency Rates Higher / Hiking (+30 Pts Quote)</option>
                                    <option value="neutral">Neutral / Parity Rates (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-pulse'></i> Inflation / CPI Data Trend</label>
                                <select id="m6Inflation">
                                    <option value="base_hot">Base CPI Hotter than Forecast (+25 Pts Base)</option>
                                    <option value="quote_hot">Quote CPI Hotter than Forecast (+25 Pts Quote)</option>
                                    <option value="aligned">Aligned with Consensus (0 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-pie-chart-alt-2'></i> Global Risk Regime</label>
                                <select id="m6RiskRegime">
                                    <option value="risk_on">Risk-On (Equities Surging, Growth Favored)</option>
                                    <option value="risk_off">Risk-Off (Geopolitical Panic, Safe Havens Favored)</option>
                                    <option value="choppy">Neutral / Mixed Market Sentiment</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-calendar'></i> High-Impact News Proximity</label>
                                <select id="m6NewsProximity">
                                    <option value="clear">No Red Folder News Today (Clear Trading)</option>
                                    <option value="upcoming">Major Red Folder Within 30 Minutes (High Risk)</option>
                                    <option value="post">Post-News (Release Occurred > 15 Mins Ago)</option>
                                </select>
                            </div>
                        </div>

                        <button class="calc-btn" onclick="evaluateMacroBias()" style="margin-top: 15px;">
                            <i class='bx bx-analyse'></i> Evaluate Macro Directional Bias
                        </button>

                        <div id="m6ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">MACRO BIAS AUDIT</div>
                                <div id="m6GradeBadge" class="badge-aaa">STRONG BULLISH BASE</div>
                            </div>
                            <div class="value" id="m6ScoreValue" style="text-align: center; font-size: 36px; margin: 15px 0;">+75 Net Bias</div>
                            <p id="m6Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m6Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 6. VIP CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 6. The VIP Macro & News Defense Checklist</h3>
                    <p>Protect your funded account against news slippage and volatility whipsaws:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Monday 10-Minute Calendar Scan:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Every Sunday evening or Monday morning, open ForexFactory and log every Red Folder event for the upcoming week.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">The 15-Minute News Embargo:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never enter a new trade within 15 minutes before or after a Tier-1 high impact release (NFP, CPI, FOMC). Spreads can widen by 20+ pips.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Trade the Aftermath, Never the Spike:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Let the initial news release sweep both sides of liquidity. Wait 15-30 minutes for the dust to settle and enter on the newly formed SMC Order Block.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Prop Firm News Compliance:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Check your prop firm rules. Many funded challenges immediately fail accounts that execute trades within 2 minutes of major news.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Monitor the US Dollar Index (DXY):</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Always check DXY structure before trading EUR/USD, GBP/USD, or Gold. If DXY is tapping key resistance, look for long setups on EUR/USD.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Correlate with Bond Yields (US10Y):</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">When 10-year US Treasury yields surge, USD/JPY rallies and Gold drops. Use bond yields as your institutional canary in the coal mine.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Never Marry a Macro Bias:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">If your technical chart shows a clean Bearish CHoCH on the H1 timeframe, do not refuse to sell just because you are macro bullish. Technicals rule execution.</p>
                    </div>
                </div>

                <!-- 7. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 6 Masterclass: Practical Fundamentals & Macro Trading</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/n4_8dFz-XyY?rel=0&modestbranding=1"
                            title="Practical Fundamentals & Macro Trading Masterclass"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 18:30:</strong> Interest Rate Differentials & Central Bank Monetary Cycles.</li>
                            <li><strong>18:31 - 36:50:</strong> The Big 3: NFP, CPI & FOMC News Trading Playbooks.</li>
                            <li><strong>36:51 - 54:15:</strong> Reading Sentiment & Avoiding News Slippage Traps.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(5)"><i class='bx bx-left-arrow-alt'></i> Previous: Entry Models</button>
                    <button class="nav-btn primary" onclick="showModule(7)">Next: Risk & Psychology <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>
"""

MODULE_7 = """            <!-- MODULE 7 -->
            <div class="module-content-pane" id="module-7">
                <div class="module-hero">
                    <span class="module-number">Capital Defense & Mindset</span>
                    <h1>Module 7: Mathematical Risk Engineering & Master Psychology</h1>
                    <p>The mathematics of asymmetry, the 40% win rate wealth engine, the 1-2-5 capital defense system, and psychological mastery.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 87.5%;"></div>
                    </div>
                </div>

                <!-- 1. THE MATH OF ASYMMETRY -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 1. The Mathematics of Asymmetry: The 40% Win Rate Wealth Engine</h3>
                    <p>Amateur traders obsess over finding a 90% win rate "holy grail" strategy. Institutional operators understand that <strong>win rate is mathematically irrelevant without Risk-to-Reward (R:R) expectancy</strong>. A trader winning only 40% of their trades with an institutional 1:3 R:R will dramatically outperform and outlast an amateur winning 80% with a 1:0.5 R:R.</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Win Rate</th>
                                    <th>Risk:Reward</th>
                                    <th>100-Trade Wins</th>
                                    <th>100-Trade Losses</th>
                                    <th>Net R-Yield</th>
                                    <th>Portfolio Return (1% Risk)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>40% (Institutional)</strong></td>
                                    <td><strong>1:3 R:R</strong></td>
                                    <td>40 Wins (+120R)</td>
                                    <td>60 Losses (-60R)</td>
                                    <td><strong>+60R</strong></td>
                                    <td><span class="badge-aaa">+60.0% NET PROFIT</span></td>
                                </tr>
                                <tr>
                                    <td><strong>40% (Sniper SMC)</strong></td>
                                    <td><strong>1:5 R:R</strong></td>
                                    <td>40 Wins (+200R)</td>
                                    <td>60 Losses (-60R)</td>
                                    <td><strong>+140R</strong></td>
                                    <td><span class="badge-aaa">+140.0% NET PROFIT</span></td>
                                </tr>
                                <tr>
                                    <td><strong>50% (Standard)</strong></td>
                                    <td><strong>1:2 R:R</strong></td>
                                    <td>50 Wins (+100R)</td>
                                    <td>50 Losses (-50R)</td>
                                    <td><strong>+50R</strong></td>
                                    <td><span class="badge-b">+50.0% NET PROFIT</span></td>
                                </tr>
                                <tr>
                                    <td><strong>80% (Retail Scalper)</strong></td>
                                    <td><strong>1:0.3 R:R</strong></td>
                                    <td>80 Wins (+24R)</td>
                                    <td>20 Losses (-20R)</td>
                                    <td><strong>+4R</strong></td>
                                    <td><span class="badge-c">+4.0% (Wiped by 1 bad loss)</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 2. THE 1-2-5 CAPITAL DEFENSE SYSTEM -->
                <div class="content-section">
                    <h3><i class='bx bx-shield-quarter'></i> 2. The 1-2-5 Capital Defense System</h3>
                    <p>Capital preservation is your primary job description. The 1-2-5 rule is the exact algorithmic risk framework used by institutional prop desks to make blowing an account mathematically impossible.</p>

                    <div class="grid-2">
                        <div class="sd-step-card">
                            <div class="sd-step-num">1%</div>
                            <strong style="color: var(--vip-gold); font-size: 14px;">1% Max Risk Per Trade:</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never risk more than 1.0% of current account equity on any single execution. On prop firm challenges, reduce this to 0.5%.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">2%</div>
                            <strong style="color: #ff9900; font-size: 14px;">2% Max Daily Loss Limit:</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">If you suffer two consecutive full 1% losses in a single day, terminal access is terminated immediately. Walk away until tomorrow.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">5%</div>
                            <strong style="color: #ff4444; font-size: 14px;">5% Max Trailing Drawdown Circuit Breaker:</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">If overall drawdown touches 5% from the peak balance, trading is halted for a full week to perform complete audit and backtesting review.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">100</div>
                            <strong style="color: #00ff88; font-size: 14px;">100 Consecutive Bullet Margin:</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">At 1% risk per trade, you require 100 consecutive full losses to hit zero. Emotional panic evaporates when you possess 100 lives.</p>
                        </div>
                    </div>
                </div>

                <!-- 3. DRAWDOWN RECOVERY NON-LINEARITY -->
                <div class="content-section">
                    <h3><i class='bx bx-line-chart-down'></i> 3. The Non-Linear Math of Drawdown Recovery</h3>
                    <p>Losses are asymmetrical. A 10% loss requires an 11% gain to break even. A 50% loss requires a staggering 100% gain just to get back to zero.</p>

                    <!-- SVG 6: Drawdown Ruin Curve -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- Grid lines -->
                                <line x1="80" y1="240" x2="750" y2="240" stroke="#333" stroke-width="1.5" />
                                <line x1="80" y1="30" x2="80" y2="240" stroke="#333" stroke-width="1.5" />

                                <!-- Curve of Ruin -->
                                <path d="M 80 240 Q 450 220 580 140 T 720 40" fill="none" stroke="#ff4444" stroke-width="3.5" />

                                <!-- Points on Curve -->
                                <circle cx="180" cy="235" r="5" fill="#00ff88" />
                                <text x="180" y="220" fill="#00ff88" font-size="10" text-anchor="middle">-10% Loss = +11% to Recover</text>

                                <circle cx="340" cy="225" r="5" fill="var(--vip-gold)" />
                                <text x="340" y="210" fill="var(--vip-gold)" font-size="10" text-anchor="middle">-20% Loss = +25% to Recover</text>

                                <circle cx="530" cy="180" r="6" fill="#ff9900" />
                                <text x="530" y="165" fill="#ff9900" font-size="11" font-weight="700" text-anchor="middle">-50% Loss = +100% to Recover</text>

                                <circle cx="680" cy="80" r="7" fill="#ff4444" />
                                <text x="680" y="65" fill="#ff4444" font-size="12" font-weight="800" text-anchor="middle">-80% Loss = +400% to Recover (Ruin)</text>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The Non-Linear Drawdown Curve: Protecting capital at early stages (-2% to -5%) is infinitely easier than digging out of a deep psychological hole.</p>
                    </div>
                </div>

                <!-- 4. THE 4 TRADER MIND TRAPS -->
                <div class="content-section">
                    <h3><i class='bx bx-brain'></i> 4. The 4 Trader Mind Traps & Psychological Neutralization</h3>
                    <p>Trading is the only profession where emotional human intuition will consistently destroy performance. You must recognize and systematically neutralize the four psychological demons:</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">1. FOMO (Fear of Missing Out)</h4>
                            <p style="font-size: 13px; line-height: 1.6;"><strong>Symptom:</strong> Jumping into a candle that has already expanded 40 pips because you are terrified of being left behind.<br><strong>Antidote:</strong> Realize that the market prints 250 trading days a year. The next setup will arrive within 24 hours.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">2. Revenge Trading</h4>
                            <p style="font-size: 13px; line-height: 1.6;"><strong>Symptom:</strong> Immediately doubling lot size after a loss to "win back" your money from the market.<br><strong>Antidote:</strong> Enforce the 2% Daily Circuit Breaker. The market does not know or care about your previous loss.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid var(--vip-gold);">
                            <h4 style="color: var(--vip-gold); margin-bottom: 8px;">3. Hesitation & Analysis Paralysis</h4>
                            <p style="font-size: 13px; line-height: 1.6;"><strong>Symptom:</strong> Staring at a textbook Grade AAA setup and freezing because your previous two trades took a loss.<br><strong>Antidote:</strong> Accept that any single trade outcome is random; only the 100-trade series has statistical edge.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">4. Euphoria & Overconfidence</h4>
                            <p style="font-size: 13px; line-height: 1.6;"><strong>Symptom:</strong> Winning 4 trades in a row and feeling invincible, leading to bloated lot sizes and ignored stop losses.<br><strong>Antidote:</strong> A winning streak is variance. Stick to the 1% risk rule religiously.</p>
                        </div>
                    </div>
                </div>

                <!-- 5. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 5. VIP Interactive Tool: Capital Defense & Drawdown Ruin Calculator</h3>
                    <p>Calculate your mathematical risk of ruin and maximum expected losing streak based on your strategy's win rate and risk allocation.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-shield'></i> Ruin Probability Simulator</h4>
                            <span class="badge-institutional">MODULE 7 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-pie-chart'></i> Historical Strategy Win Rate (%)</label>
                                <input type="number" id="m7WinRate" value="45" min="20" max="85" step="1">
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-target-lock'></i> Average Risk:Reward Ratio (1:X)</label>
                                <input type="number" id="m7RR" value="3.5" min="1.0" max="10.0" step="0.5">
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-dollar'></i> Risk Percentage Per Trade (%)</label>
                                <select id="m7RiskPct">
                                    <option value="0.5">0.5% (Prop Firm Recommended)</option>
                                    <option value="1.0" selected>1.0% (Standard Institutional Risk)</option>
                                    <option value="2.0">2.0% (Aggressive Personal Account)</option>
                                    <option value="5.0">5.0% (Reckless / High Ruin Probability)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-error-circle'></i> Max Drawdown Limit to Ruin (%)</label>
                                <input type="number" id="m7MaxDD" value="10" min="4" max="50">
                            </div>
                        </div>

                        <button class="calc-btn" onclick="calculateDrawdownRuin()" style="margin-top: 15px;">
                            <i class='bx bx-analyse'></i> Calculate Risk of Ruin & Expectancy
                        </button>

                        <div id="m7ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">MATHEMATICAL RUIN AUDIT</div>
                                <div id="m7GradeBadge" class="badge-aaa">IMPOSSIBLE RUIN (< 0.01%)</div>
                            </div>
                            <div class="value" id="m7ExpectancyValue" style="text-align: center; font-size: 36px; margin: 15px 0;">+1.025 R / Trade</div>
                            <p id="m7Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m7Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 6. VIP CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 6. The VIP Psychological & Risk Defense Checklist</h3>
                    <p>Your mental firewall against emotional tilt:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Pre-Session Emotional State Audit:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">If you are tired, angry, stressed, or sick, do not open MT4/TradingView. A compromised mind cannot execute probabilistic edge.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Strict 2-Loss Daily Lockdown:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Two losses in a day triggers an immediate shutdown. No exceptions. Come back tomorrow with a clean slate.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Never Move Stops Away:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Widening a stop loss during a trade to "give it more room" is the number one cause of blown funded accounts. Accept the planned loss.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Lot Size Calculated Before Every Order:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Always plug your stop-loss pips into the Pro Toolbox Position Sizer. Never guess lot size based on "how confident" you feel.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Detached Execution:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Once your limit order or confirmation entry is active, close the chart. Staring at every 1-minute tick induces panic and micromanagement.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Think in Blocks of 25 Trades:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Judge your performance solely across blocks of 25 consecutive setups executed strictly according to plan.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Withdrawal Mindset:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">A profit is not real until it leaves the broker/prop firm account and arrives in your physical bank account.</p>
                    </div>
                </div>

                <!-- 7. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 7 Masterclass: Risk Engineering & Psychological Mastery</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/RzjKKaLlY0s?rel=0&modestbranding=1"
                            title="Risk Engineering & Psychological Mastery Masterclass"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 19:40:</strong> The Mathematical Proof of Asymmetric R:R Wealth Creation.</li>
                            <li><strong>19:41 - 38:10:</strong> The 1-2-5 Capital Defense System & Drawdown Ruin Mechanics.</li>
                            <li><strong>38:11 - 58:20:</strong> Eradicating FOMO, Revenge Trading & Overconfidence.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(6)"><i class='bx bx-left-arrow-alt'></i> Previous: Fundamentals</button>
                    <button class="nav-btn primary" onclick="showModule(8)">Next: Business Model <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>
"""

print("Module 6 and Module 7 compiled.")
