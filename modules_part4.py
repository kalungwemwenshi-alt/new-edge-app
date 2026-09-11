# modules_part4.py
# Comprehensive content for Module 8 & Module 9

MODULE_8 = """            <!-- MODULE 8 -->
            <div class="module-content-pane" id="module-8">
                <div class="module-hero">
                    <span class="module-number">Capital Scaling</span>
                    <h1>Module 8: Professional Trading as a Business & Prop Firm Scaling</h1>
                    <p>Treating trading as an inventory business, passing prop firm evaluations, trailing drawdown mechanics, and the 4-stage capital scaling roadmap.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 95%;"></div>
                    </div>
                </div>

                <!-- 1. TRADING AS AN INVENTORY BUSINESS -->
                <div class="content-section">
                    <h3><i class='bx bx-briefcase'></i> 1. The Operating Mindset: Trading as an Inventory Business</h3>
                    <p>A hobby trader asks: <em>"How much money can I make today?"</em> An institutional operator asks: <em>"What is my cost of inventory, what is my maximum allowable risk exposure, and what is my statistical edge over the next 100 transactions?"</em></p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid var(--vip-gold);">
                            <h4 style="color: var(--vip-gold); margin-bottom: 8px;">The Retail Hobbyist</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Gambles personal life savings on high leverage. Experiences severe emotional swings. Never collects data. Views a losing trade as personal failure.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">The Enterprise Business Operator</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Trades other people's capital (prop firms & institutional investors). Treats stopped-out trades as wholesale Cost of Goods Sold (COGS). Extracts monthly dividends and diversifies into tangible assets.</p>
                        </div>
                    </div>
                </div>

                <!-- 2. PROP FIRM EVALUATION DECODED -->
                <div class="content-section">
                    <h3><i class='bx bx-buildings'></i> 2. Prop Firm Evaluations Decoded: Passing Blueprint</h3>
                    <p>Proprietary trading firms offer modern traders access to $100,000 to $1,000,000+ in funded liquidity. However, 92% of applicants fail due to misunderstanding <strong>daily vs trailing maximum drawdown algorithms</strong>.</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Evaluation Phase</th>
                                    <th>Profit Target</th>
                                    <th>Daily Loss Limit</th>
                                    <th>Max Overall Drawdown</th>
                                    <th>Risk-Per-Trade Protocol</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Phase 1 (Challenge)</strong></td>
                                    <td>8.0% - 10.0%</td>
                                    <td>4.0% - 5.0% (Strict)</td>
                                    <td>8.0% - 10.0% (Static/Trailing)</td>
                                    <td>0.5% - 0.75% per setup</td>
                                </tr>
                                <tr>
                                    <td><strong>Phase 2 (Verification)</strong></td>
                                    <td>5.0%</td>
                                    <td>4.0% - 5.0% (Strict)</td>
                                    <td>8.0% - 10.0%</td>
                                    <td>0.5% per setup (Defensive)</td>
                                </tr>
                                <tr>
                                    <td><strong>Live Funded Account</strong></td>
                                    <td>Zero (Payout Target)</td>
                                    <td>4.0% - 5.0%</td>
                                    <td>8.0% - 10.0% (Buffer Locked)</td>
                                    <td>0.25% - 0.5% (Max Capital Preservation)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="key-takeaways" style="margin-top: 25px;">
                        <h4>The Trailing High-Water Mark Drawdown Trap</h4>
                        <p style="font-size: 13px; color: #ccc;">On trailing drawdown models, if your $100,000 account hits $106,000 in floating equity, your maximum loss limit trails upward to $101,000. If you do not lock in profits and let the trade retrace to $100,500, you are instantly disqualified! Always know whether your firm uses <strong>Balance-Based</strong> (safe) or <strong>Equity-Based Trailing</strong> (high-friction) drawdown.</p>
                    </div>
                </div>

                <!-- 3. THE 4-STAGE CAPITAL SCALING ROADMAP -->
                <div class="content-section">
                    <h3><i class='bx bx-trending-up'></i> 3. The 4-Stage Capital Scaling Roadmap ($25k to $1M+)</h3>
                    <p>Do not attempt to trade a $500,000 account on day one. Follow the EdgeGrid systematic capital scaling pathway:</p>

                    <!-- SVG 7: Scaling Pyramid -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- Stage 4 Apex -->
                                <polygon points="400,30 490,90 310,90" fill="rgba(214, 255, 0, 0.2)" stroke="var(--vip-gold)" stroke-width="2" />
                                <text x="400" y="60" fill="var(--vip-gold)" font-size="13" font-weight="800" text-anchor="middle">STAGE 4: $1,000,000+ ENTERPRISE</text>
                                <text x="400" y="78" fill="#ddd" font-size="9" text-anchor="middle">Multi-Firm Portfolio + Trade Copiers ($30k - $60k/mo)</text>

                                <!-- Stage 3 -->
                                <polygon points="310,95 490,95 560,165 240,165" fill="rgba(0, 255, 136, 0.12)" stroke="#00ff88" stroke-width="1.5" />
                                <text x="400" y="125" fill="#00ff88" font-size="13" font-weight="700" text-anchor="middle">STAGE 3: $300,000 PORTFOLIO</text>
                                <text x="400" y="145" fill="#aaa" font-size="9" text-anchor="middle">3x $100k Funded Accounts with Split Risk ($10k - $20k/mo)</text>

                                <!-- Stage 2 -->
                                <polygon points="240,170 560,170 630,240 170,240" fill="rgba(0, 191, 255, 0.1)" stroke="#00bfff" stroke-width="1.5" />
                                <text x="400" y="200" fill="#00bfff" font-size="13" font-weight="700" text-anchor="middle">STAGE 2: $100,000 CONSOLIDATION</text>
                                <text x="400" y="220" fill="#aaa" font-size="9" text-anchor="middle">First Full-Scale Funded Account ($4,000 - $8,000/mo Payouts)</text>

                                <!-- Stage 1 Base -->
                                <rect x="120" y="248" width="560" height="52" fill="rgba(255, 255, 255, 0.05)" stroke="#666" stroke-width="1.5" rx="6" />
                                <text x="400" y="275" fill="#FFFFFF" font-size="13" font-weight="800" text-anchor="middle">STAGE 1: $25,000 PROVING GROUND</text>
                                <text x="400" y="292" fill="#aaa" font-size="10" text-anchor="middle">Mastering Verification Discipline & Achieving 1st Bi-Weekly Payout</text>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The 4-Stage Scaling Pathway: Pass the $25k test first to cement your execution psychology, then scale laterally across reputable prop firms.</p>
                    </div>
                </div>

                <!-- 4. THE 80/20 PROFIT EXTRACTION RULE -->
                <div class="content-section">
                    <h3><i class='bx bx-wallet'></i> 4. The 80/20 Profit Withdrawal & Wealth Rule</h3>
                    <p>Never leave 100% of your earnings inside prop firm accounts. Prop firms can change terms or cease operations overnight. Follow the <strong>80/20 Profit Withdrawal Protocol</strong>:</p>

                    <div class="grid-2">
                        <div class="sd-step-card">
                            <div class="sd-step-num">80%</div>
                            <strong style="color: #00ff88; font-size: 14px;">80% Physical Withdrawal:</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Upon every bi-weekly payout, withdraw 80% directly into your local bank or secure cold-storage cryptocurrency wallet. Convert into cash and tangible investments.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">20%</div>
                            <strong style="color: var(--vip-gold); font-size: 14px;">20% Buffer & Challenge Reinvestment:</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Allocate 20% of your earnings to purchase fresh challenges at secondary firms, creating redundancy and expanding your total allocation.</p>
                        </div>
                    </div>
                </div>

                <!-- 5. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 5. VIP Interactive Tool: Prop Firm Scaling & Drawdown Planner</h3>
                    <p>Calculate your daily risk allowance, number of winning trades required to pass, and project your monthly take-home payouts.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-buildings'></i> Prop Firm Capital Planner</h4>
                            <span class="badge-institutional">MODULE 8 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-dollar-circle'></i> Funded Account Size ($)</label>
                                <select id="m8AccountSize">
                                    <option value="25000">$25,000 (Stage 1)</option>
                                    <option value="50000">$50,000 (Intermediate)</option>
                                    <option value="100000" selected>$100,000 (Standard Tier-1)</option>
                                    <option value="200000">$200,000 (Advanced)</option>
                                    <option value="500000">$500,000 (Enterprise Multi-Firm)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-shield-quarter'></i> Max Daily Loss Allowance (%)</label>
                                <select id="m8DailyLoss">
                                    <option value="4.0">4.0% Daily Loss Limit</option>
                                    <option value="5.0" selected>5.0% Daily Loss Limit</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-target-lock'></i> Risk Per Trade (%)</label>
                                <select id="m8RiskPerTrade">
                                    <option value="0.25">0.25% (Ultra-Safe / High Longevity)</option>
                                    <option value="0.5" selected>0.50% (Recommended Standard)</option>
                                    <option value="1.0">1.00% (Aggressive)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-pie-chart-alt'></i> Monthly Target Return (%)</label>
                                <input type="number" id="m8MonthlyTarget" value="6.0" min="2.0" max="20.0" step="0.5">
                            </div>
                        </div>

                        <button class="calc-btn" onclick="planPropFirmScaling()" style="margin-top: 15px;">
                            <i class='bx bx-calculator'></i> Calculate Risk Limits & Payout Projections
                        </button>

                        <div id="m8ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">SCALING PARAMETER AUDIT</div>
                                <div id="m8GradeBadge" class="badge-aaa">OPTIMAL CAPITAL ALLOCATION</div>
                            </div>
                            <div class="value" id="m8MonthlyPayout" style="text-align: center; font-size: 36px; margin: 15px 0;">$4,800 / Month Payout</div>
                            <p id="m8Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m8Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 6. VIP CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 6. The VIP Funded Trader Operating Checklist</h3>
                    <p>Strict operational compliance to guarantee funded longevity:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Know the Drawdown Calculation Method:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never trade a prop account without knowing if daily loss is calculated from the start-of-day balance or equity.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Halve Your Risk in Drawdown:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">If your account drops 2% into drawdown, reduce your risk per trade from 0.5% down to 0.25% until back at break-even.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Weekend Holding Verification:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Always close open positions by Friday 20:00 GMT unless your specific challenge model explicitly permits weekend holding.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Diversify Across Multiple Firms:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never hold your entire allocation in a single prop firm. Split capital across at least 2 or 3 reputable providers.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Maintain a Trade Journal with Screenshots:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Save before/after chart screenshots of every setup. If a prop firm disputes an execution, your journal provides proof of manual compliance.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Withdraw First Payout Immediately:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">The moment your first bi-weekly payout window opens, request withdrawal. Recover your challenge fee immediately to become 100% risk-free.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Never Trade During Payout Processing:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Some firms will void a pending payout if you take a loss while the withdrawal is being processed. Stand aside until funds arrive.</p>
                    </div>
                </div>

                <!-- 7. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 8 Masterclass: Professional Trading as a Business & Prop Firm Scaling</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/5Dq93fGvQk0?rel=0&modestbranding=1"
                            title="Professional Trading Business Model Masterclass"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 18:25:</strong> Operating Trading as an Enterprise Business.</li>
                            <li><strong>18:26 - 37:45:</strong> Deconstructing Prop Firm Trailing Drawdowns & Evaluation Strategies.</li>
                            <li><strong>37:46 - 55:30:</strong> The 4-Stage Capital Scaling Roadmap to $1,000,000+.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(7)"><i class='bx bx-left-arrow-alt'></i> Previous: Risk & Psychology</button>
                    <button class="nav-btn primary" onclick="showModule(9)">Next: Backtesting & Strategy <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>
"""

MODULE_9 = """            <!-- MODULE 9 -->
            <div class="module-content-pane" id="module-9">
                <div class="module-hero">
                    <span class="module-number">Strategy Synthesis</span>
                    <h1>Module 9: Strategy Synthesis, Rigorous Backtesting & Live Blueprint</h1>
                    <p>The scientific backtesting protocol, complete A-to-Z SMC execution plan, the daily operating routine, and capstone certification.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 100%;"></div>
                    </div>
                </div>

                <!-- 1. THE SCIENTIFIC BACKTESTING PROTOCOL -->
                <div class="content-section">
                    <h3><i class='bx bx-test-tube'></i> 1. The Scientific Backtesting Protocol (Law of 100 Samples)</h3>
                    <p>Testing a strategy on 10 trades tells you nothing; it is statistically indistinguishable from a coin flip. To prove mathematical expectancy, an institutional operator executes a <strong>rigorous 100-sample backtest</strong> with fixed variable isolation.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid var(--vip-gold);">
                            <h4 style="color: var(--vip-gold); margin-bottom: 8px;">The 5 Core Metrics Every Operator Must Audit</h4>
                            <ul style="font-size: 13px; line-height: 1.6; color: var(--vip-text-muted); padding-left: 18px;">
                                <li><strong>1. Mathematical Expectancy:</strong> Average R won per trade across the entire 100-sample series.</li>
                                <li><strong>2. Profit Factor:</strong> (Gross Profits / Gross Losses). Must be > 2.0 for institutional deployment.</li>
                                <li><strong>3. Maximum Drawdown Streak:</strong> Longest consecutive losing streak observed.</li>
                                <li><strong>4. Average Risk:Reward:</strong> Must be at least 1:3.0.</li>
                                <li><strong>5. MAE & MFE:</strong> Maximum Adverse Excursion and Maximum Favorable Excursion.</li>
                            </ul>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">The Forward Testing & Demo Incubation Phase</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Once 100 historical setups confirm expectancy, you must execute <strong>30 live forward trades on a demo account</strong> during real session kill zones. This proves that you can identify setups in real time with live execution latency and emotional detachment.</p>
                        </div>
                    </div>
                </div>

                <!-- 2. THE COMPLETE EDGEGRID MASTER TRADING PLAN -->
                <div class="content-section">
                    <h3><i class='bx bx-sitemap'></i> 2. The Complete EdgeGrid Master Execution Flowchart</h3>
                    <p>The complete end-to-end algorithmic decision tree from Higher Timeframe narrative down to Trade Management:</p>

                    <!-- SVG 8: Execution Flowchart -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- Step 1 Box -->
                                <rect x="30" y="40" width="160" height="70" fill="rgba(214, 255, 0, 0.12)" stroke="var(--vip-gold)" stroke-width="1.5" rx="6" />
                                <text x="110" y="65" fill="var(--vip-gold)" font-size="11" font-weight="800" text-anchor="middle">1. HTF NARRATIVE</text>
                                <text x="110" y="82" fill="#ddd" font-size="9" text-anchor="middle">Daily / H4 Structure</text>
                                <text x="110" y="96" fill="#aaa" font-size="8" text-anchor="middle">Premium / Discount Filter</text>

                                <!-- Arrow 1 -->
                                <path d="M 190 75 L 230 75" stroke="var(--vip-gold)" stroke-width="2" marker-end="url(#m9ArrowGold)" />

                                <!-- Step 2 Box -->
                                <rect x="230" y="40" width="160" height="70" fill="rgba(0, 255, 136, 0.12)" stroke="#00ff88" stroke-width="1.5" rx="6" />
                                <text x="310" y="65" fill="#00ff88" font-size="11" font-weight="800" text-anchor="middle">2. KEY POI & LIQUIDITY</text>
                                <text x="310" y="82" fill="#ddd" font-size="9" text-anchor="middle">Unmitigated OB / FVG</text>
                                <text x="310" y="96" fill="#aaa" font-size="8" text-anchor="middle">Target BSL/SSL Swept</text>

                                <!-- Arrow 2 -->
                                <path d="M 390 75 L 430 75" stroke="#00ff88" stroke-width="2" marker-end="url(#m9ArrowGreen)" />

                                <!-- Step 3 Box -->
                                <rect x="430" y="40" width="160" height="70" fill="rgba(0, 191, 255, 0.12)" stroke="#00bfff" stroke-width="1.5" rx="6" />
                                <text x="510" y="65" fill="#00bfff" font-size="11" font-weight="800" text-anchor="middle">3. SESSION KILL ZONE</text>
                                <text x="510" y="82" fill="#ddd" font-size="9" text-anchor="middle">London (07:00-10:00 GMT)</text>
                                <text x="510" y="96" fill="#aaa" font-size="8" text-anchor="middle">NY AM (12:00-15:00 GMT)</text>

                                <!-- Arrow 3 Down -->
                                <path d="M 510 110 L 510 160" stroke="#00bfff" stroke-width="2" marker-end="url(#m9ArrowCyan)" />

                                <!-- Step 4 Box -->
                                <rect x="430" y="160" width="160" height="70" fill="rgba(255, 68, 68, 0.12)" stroke="#ff4444" stroke-width="1.5" rx="6" />
                                <text x="510" y="185" fill="#ff4444" font-size="11" font-weight="800" text-anchor="middle">4. LTF CONFIRMATION</text>
                                <text x="510" y="202" fill="#ddd" font-size="9" text-anchor="middle">M5 / M1 Liquidity Sweep</text>
                                <text x="510" y="216" fill="#aaa" font-size="8" text-anchor="middle">CHoCH + Displacement FVG</text>

                                <!-- Arrow 4 Left -->
                                <path d="M 430 195 L 390 195" stroke="#ff4444" stroke-width="2" marker-end="url(#m9ArrowRed)" />

                                <!-- Step 5 Box -->
                                <rect x="230" y="160" width="160" height="70" fill="rgba(214, 255, 0, 0.15)" stroke="var(--vip-gold)" stroke-width="2" rx="6" />
                                <text x="310" y="185" fill="var(--vip-gold)" font-size="11" font-weight="800" text-anchor="middle">5. EXECUTION & RISK</text>
                                <text x="310" y="202" fill="#ddd" font-size="9" text-anchor="middle">1% Fixed Position Size</text>
                                <text x="310" y="216" fill="#aaa" font-size="8" text-anchor="middle">Stop Loss 2 Pips Past Distal</text>

                                <!-- Arrow 5 Left -->
                                <path d="M 230 195 L 190 195" stroke="var(--vip-gold)" stroke-width="2" marker-end="url(#m9ArrowGold)" />

                                <!-- Step 6 Box -->
                                <rect x="30" y="160" width="160" height="70" fill="rgba(0, 255, 136, 0.2)" stroke="#00ff88" stroke-width="2" rx="6" />
                                <text x="110" y="185" fill="#00ff88" font-size="11" font-weight="800" text-anchor="middle">6. HARVEST (1:4+ R:R)</text>
                                <text x="110" y="202" fill="#ddd" font-size="9" text-anchor="middle">50% Partials at 2R / BE</text>
                                <text x="110" y="216" fill="#aaa" font-size="8" text-anchor="middle">Runners Target External BSL/SSL</text>

                                <defs>
                                    <marker id="m9ArrowGold" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M 0 0 L 8 4 L 0 8 Z" fill="var(--vip-gold)" /></marker>
                                    <marker id="m9ArrowGreen" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M 0 0 L 8 4 L 0 8 Z" fill="#00ff88" /></marker>
                                    <marker id="m9ArrowCyan" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M 0 0 L 8 4 L 0 8 Z" fill="#00bfff" /></marker>
                                    <marker id="m9ArrowRed" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M 8 0 L 0 4 L 8 8 Z" fill="#ff4444" /></marker>
                                </defs>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The EdgeGrid Master Decision Matrix: Every trade must seamlessly progress through all 6 operational checkpoints.</p>
                    </div>
                </div>

                <!-- 3. THE DAILY OPERATING ROUTINE -->
                <div class="content-section">
                    <h3><i class='bx bx-calendar-check'></i> 3. The Professional Trader's Daily Operating Routine</h3>
                    <p>Consistency in results requires consistency in routine. A high-performance trading day is strictly partitioned into three phases:</p>

                    <div class="grid-2">
                        <div class="sd-step-card">
                            <div class="sd-step-num">AM</div>
                            <strong style="color: var(--vip-gold); font-size: 14px;">Phase 1: Pre-Market Recon (06:00 - 07:00 UTC)</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Review economic calendar for Red Folder news. Mark previous day's high/low (PDH/PDL) and box the Asian session range on EUR/USD, GBP/USD, and Gold.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">LIVE</div>
                            <strong style="color: #00ff88; font-size: 14px;">Phase 2: Live Kill Zone Execution (07:00 - 15:00 UTC)</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Monitor price action during London Open and NY AM. Wait for liquidity sweep and confirmation CHoCH. Execute strictly with calculated position sizes.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">PM</div>
                            <strong style="color: #00bfff; font-size: 14px;">Phase 3: Post-Market Debrief & Journal (19:00 - 20:00 UTC)</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Log all executions into your trading journal. Attach before/after chart screenshots, record R-yield, and grade execution compliance from 1 to 10.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">OFF</div>
                            <strong style="color: #ff4444; font-size: 14px;">Phase 4: Mental Detachment (Evening)</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Close all charts. No scrolling through crypto or forex social media. Rest, exercise, and recharge cognitive stamina for tomorrow.</p>
                        </div>
                    </div>
                </div>

                <!-- 4. COMPARISON BENCHMARK TABLE -->
                <div class="content-section">
                    <h3><i class='bx bx-table'></i> 4. EdgeGrid VIP Strategy Performance Benchmark</h3>
                    <p>Standardized institutional metrics expected across various SMC setups:</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Setup Archetype</th>
                                    <th>Weekly Frequency</th>
                                    <th>Observed Win Rate</th>
                                    <th>Average R:R</th>
                                    <th>Expected Monthly Yield</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>London Judas Sweep + CHoCH</strong></td>
                                    <td>3 - 5 Setups</td>
                                    <td>72% - 78%</td>
                                    <td>1:4.5 R:R</td>
                                    <td><span class="badge-aaa">+8R to +15R / Month</span></td>
                                </tr>
                                <tr>
                                    <td><strong>NY AM Open Continuation (FVG)</strong></td>
                                    <td>4 - 6 Setups</td>
                                    <td>68% - 74%</td>
                                    <td>1:3.5 R:R</td>
                                    <td><span class="badge-aaa">+6R to +12R / Month</span></td>
                                </tr>
                                <tr>
                                    <td><strong>HTF Breaker Block Reversal</strong></td>
                                    <td>1 - 2 Setups</td>
                                    <td>65% - 70%</td>
                                    <td>1:6.0+ R:R</td>
                                    <td><span class="badge-b">+5R to +10R / Month</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 5. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 5. VIP Interactive Tool: Strategy Backtest Statistical Validator</h3>
                    <p>Input your 50 or 100-trade backtesting sample data to calculate mathematical expectancy, profit factor, and sample significance.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-test-tube'></i> Strategy Expectancy Validator</h4>
                            <span class="badge-institutional">MODULE 9 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-list-check'></i> Total Sample Size (Trades)</label>
                                <input type="number" id="m9SampleTrades" value="100" min="25" max="500">
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-check-circle'></i> Winning Trades Count</label>
                                <input type="number" id="m9Wins" value="48" min="5" max="450">
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-target-lock'></i> Average Win Size (R-Multiple)</label>
                                <input type="number" id="m9AvgWin" value="3.8" min="1.0" max="15.0" step="0.1">
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-x-circle'></i> Average Loss Size (R-Multiple)</label>
                                <input type="number" id="m9AvgLoss" value="1.0" min="0.5" max="3.0" step="0.1">
                            </div>
                        </div>

                        <button class="calc-btn" onclick="validateBacktestStats()" style="margin-top: 15px;">
                            <i class='bx bx-analyse'></i> Validate Strategy Statistical Edge
                        </button>

                        <div id="m9ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">STATISTICAL EDGE AUDIT</div>
                                <div id="m9GradeBadge" class="badge-aaa">VERIFIED INSTITUTIONAL EDGE</div>
                            </div>
                            <div class="value" id="m9Expectancy" style="text-align: center; font-size: 36px; margin: 15px 0;">+1.30 R / Trade</div>
                            <p id="m9Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m9Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 6. VIP GRADUATION CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 6. The EdgeGrid VIP Graduation & Live Blueprint Checklist</h3>
                    <p>The 7 golden commandments of certified EdgeGrid Inner Circle operators:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">100-Trade Empirical Proof:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never trade real money until you have logged 100 historical setups proving positive mathematical expectancy (> +0.5R/trade).</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Kill Zone Exclusivity:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Only execute during London Open (07:00-10:00 GMT) or NY AM (12:00-15:00 GMT). Do not trade off-hours chop.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Liquidity-First Protocol:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Before entering, always verify that external liquidity (BSL or SSL) has been swept.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">1% Strict Sizing:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Calculate exact lot sizes before every trade. Never risk more than 1.0% (or 0.5% on prop accounts).</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">2-Loss Daily Lockdown:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Two losses in a single day terminates trading until tomorrow morning. Protect psychological capital.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Partial Scaling at 2R:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Secure 50% profits at 1:3 R:R and shift stops to Breakeven after structural confirmation.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Journal & Withdraw Regularly:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Maintain flawless journal documentation and withdraw 80% of payouts into tangible physical wealth.</p>
                    </div>
                </div>

                <!-- 7. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 9 Masterclass: Backtesting & Strategy Creation</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/RzjKKaLlY0s?rel=0&modestbranding=1"
                            title="Backtesting Forex Strategy Journal"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 15:40:</strong> The 100-Sample Backtesting Protocol & Variable Control.</li>
                            <li><strong>15:41 - 34:10:</strong> The Synthesized EdgeGrid Master Playbook from A to Z.</li>
                            <li><strong>34:11 - 52:00:</strong> High-Performance Daily Routine & Final Inner Circle Certification.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(8)"><i class='bx bx-left-arrow-alt'></i> Previous: Business Model</button>
                    <button class="nav-btn primary" onclick="showModule('tools')">Pro Trading Toolbox <i class='bx bx-wrench'></i></button>
                    <button class="nav-btn" style="background: rgba(0,255,136,0.15); color: #00ff88; border-color: #00ff88;"
                        onclick="alert('Congratulations! You have completed all 9 modules of the EdgeGrid VIP Mastery Programme. Use the Pro Toolbox next to calculate your risk!')">Programme Complete <i class='bx bx-check-double'></i></button>
                </div>
            </div>
"""

print("Module 8 and Module 9 compiled.")
